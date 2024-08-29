let pyodide = null;

async function loadPyodideAndPackages() {
    try {
        pyodide = await loadPyodide();
        await pyodide.loadPackage(['numpy' ,'pandas', 'scikit-learn']);
        console.log("Pyodide and packages loaded successfully.");
    } catch (error) {
        console.error("Error loading Pyodide or packages:", error);
        document.getElementById("output").textContent = "Error loading Pyodide or packages.";
    }
}

loadPyodideAndPackages();

function initializeCodeMirror(editorId, textareaId, valstring, lineno) {
    let codeMirror = CodeMirror(document.getElementById(editorId), {
        mode: 'python',
        theme: 'monokai',
        lineNumbers: lineno,
        value: valstring,
        extraKeys: { "Ctrl-Space": "autocomplete" }
    });

    // Sync CodeMirror content with hidden textarea
    codeMirror.on('change', function() {
        document.getElementById(textareaId).value = codeMirror.getValue();
        highlightCode();  // Assuming you have a highlightCode function
    });

    return codeMirror;
}

async function runPythonCode(editor, outputId) {
    if (!pyodide) {
        document.getElementById(outputId).textContent = "Pyodide is not loaded yet!";
        return;
    }

    // Clear the output box
    document.getElementById(outputId).textContent = "";
    
    let code = editor.getValue();

    try {
        let result = pyodide.runPython(`
            import sys
            from io import StringIO

            old_stdout = sys.stdout
            new_stdout = StringIO()
            sys.stdout = new_stdout

            try:
                exec(${JSON.stringify(code)})
            finally:
                sys.stdout = old_stdout

            output = new_stdout.getvalue()
            output
        `);

        let formattedOutput = result.split('\n').map(line => '>>> ' + line).join('\n');
        document.getElementById(outputId).textContent += formattedOutput;

    } catch (err) {
        console.error("Error running Python code:", err);
        // document.getElementById(outputId).textContent = "Error running Python code.";
        document.getElementById(outputId).textContent = "Execution error: " + err;
    }
}

// Get the button
var backToTopBtn = document.getElementById("backToTopBtn");
// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {
    scrollFunction();
};
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        backToTopBtn.style.display = "block";
    } else {
        backToTopBtn.style.display = "none";
    }
}
// When the user clicks on the button, scroll to the top of the document
function scrollToTop() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
}

document.addEventListener('scroll', function() {
    const toc = document.getElementById('toc');
    const showTocThreshold = 100; // Adjust this value as needed

    if (window.scrollY > showTocThreshold) {
        toc.style.display = 'block'; // Show the TOC
    } else {
        toc.style.display = 'none'; // Hide the TOC
    }
});