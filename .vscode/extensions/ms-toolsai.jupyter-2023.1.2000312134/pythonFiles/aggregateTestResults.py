# %%
import io
import json
import sys
import zipfile

import requests

authtoken = sys.argv[1]
print("Using authtoken with prefix: " + authtoken[:4])

# %%
def getRuns(createdDate):
    runsResponse = requests.get(
        "https://api.github.com/repos/microsoft/vscode-jupyter/actions/workflows/build-test.yml/runs",
        params={"created": createdDate, "branch": "main"},
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {authtoken}",
        },
    )

    if runsResponse.status_code != 200:
        print(f"Error {runsResponse.status_code}")
        raise Exception("Error getting runs")

    runs = runsResponse.json()["workflow_runs"]

    for run in runs:
        print(f"Found run {run['id']} for event '{run['event']}'")

    return runs


def getArtifactData(id):
    testResultsResponse = requests.get(
        f"https://api.github.com/repos/microsoft/vscode-jupyter/actions/artifacts/{id}/zip",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {authtoken}",
        },
    )

    if testResultsResponse.status_code != 200:
        print(f"Error {testResultsResponse.status_code} getting artifact {id}")

    return testResultsResponse.content


def getResultsJson(zipData):
    artifact = zipfile.ZipFile(io.BytesIO(zipData))
    for name in artifact.namelist():
        if name.endswith("results.json"):
            print(f"    parsing {name} from artifact with {artifact.namelist()}")
            return json.loads(artifact.read(name))
    else:
        print("No results.json found in artifact")
        return []


def getResultsForRun(run):
    url = run["artifacts_url"]
    print(f"Getting artifacts from {url}")
    artifactsResponse = requests.get(
        url, headers={"Accept": "application/vnd.github+json"}
    )

    if artifactsResponse.status_code != 200:
        print(f"Error {artifactsResponse.status_code} getting artifacts")
        return []

    artifacts = artifactsResponse.json()["artifacts"]

    results = []
    for artifact in artifacts:
        if (
            artifact["name"].startswith(
                "TestResult-"  # previous artifact name (pre ~2022-09-12)
            )
            or artifact["name"].startswith(
                "TestResults-"  # previous performance tests artifact name
            )
            or artifact["name"].startswith(
                "TestLogs-"  # consolidated artifact name, contains multiple files
            )
        ):
            print(f"    retrieving {artifact['name']}")
            rawData = getArtifactData(artifact["id"])
            testRunResults = getResultsJson(rawData)
            results.append(
                {
                    "scenario": artifact["name"],
                    "date": run["created_at"],
                    "runUrl": run["html_url"],
                    "data": testRunResults,
                }
            )
            print(f"    {len(testRunResults)} results read")

    return results


def flattenTestResultsToFile(runResults, filename):
    resultCount = 1
    delimiter = ""
    with open(filename, "w") as outfile:
        outfile.write("[\n")
        for runResult in runResults:
            print(f"writing results {resultCount} of {len(runResults)}")
            resultCount += 1
            for scenario in runResult:
                suite = []
                for testResult in scenario["data"]:
                    if (
                        testResult["event"] == "suite"
                        and len(str.strip(testResult["title"])) > 0
                    ):
                        suite.append(testResult["title"])
                    elif (
                        testResult["event"] == "suite end"
                        and len(str.strip(testResult["title"]))
                        and len(suite) > 0
                    ):
                        suite.pop()
                    elif "title" in testResult and "state" in testResult:
                        outfile.write(delimiter)
                        singleResult = {
                            "scenario": scenario["scenario"],
                            "suite": " - ".join(suite),
                            "testName": testResult["title"],
                            "date": scenario["date"],
                            "runUrl": scenario["runUrl"],
                            "status": testResult["state"],
                        }
                        if "duration" in testResult:
                            singleResult["duration"] = testResult["duration"]
                        outfile.write(json.dumps(singleResult))
                        delimiter = ",\n"

        outfile.write("\n]\n")


# %%
from datetime import date, datetime, timedelta

inputDate = ""
if len(sys.argv) > 2:
    inputDate = sys.argv[2]

try:
    collectionDateTime = datetime.strptime(inputDate, "%Y-%m-%d")
    collectionDate = date.fromtimestamp(collectionDateTime.timestamp())
except ValueError:
    print(
        f"The string {inputDate} is not a date with format yyyy-mm-dd, running for yesterday"
    )
    collectionDate = date.today() - timedelta(days=1)

# %%
runs = getRuns(collectionDate)

# %%
runResults = []
for run in runs:
    runResults.append(getResultsForRun(run))

# %%
resultFile = f'AggTestResults-{collectionDate.strftime("%Y-%m-%d")}.json'
allTests = flattenTestResultsToFile(runResults, resultFile)

# %%
import os

file_size = os.path.getsize(resultFile)
print(f"Wrote {file_size} bytes to {resultFile}")

# %%
