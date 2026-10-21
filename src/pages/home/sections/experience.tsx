import { FaGraduationCap, FaBriefcase } from "react-icons/fa6";

import { ScrollArea } from "@/components/ui/scroll-area";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

import { education } from "@/data/education";
import { workExperience } from "@/data/workExperience";

export default function ExperienceSection() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
      <Card className="rounded-md md:px-2">
        <CardHeader>
          <CardTitle className="flex flex-row justify-center items-center gap-2 text-plus">
            <FaGraduationCap />
            Education
          </CardTitle>
        </CardHeader>
        <ScrollArea className="max-h-96">
          <CardContent className="space-y-4">
            {education.map((edu, index) => (
              <div key={index} className="flex items-center gap-4">
                <img
                  src={edu.logo}
                  alt={`${edu.school} logo`}
                  className="w-12 h-12 object-contain rounded"
                  loading="lazy"
                />
                <div>
                  <div className="font-semibold">{edu.school}</div>
                  <div className="text-sm text-muted-foreground">
                    {edu.years}
                  </div>
                  <div className="text-sm">{edu.degree}</div>
                </div>
              </div>
            ))}
          </CardContent>
        </ScrollArea>
      </Card>

      <Card className="rounded-md md:px-2">
        <CardHeader>
          <CardTitle className="flex flex-row justify-center items-center gap-2 text-plus">
            <FaBriefcase />
            Work Experiences
          </CardTitle>
        </CardHeader>
        <ScrollArea className="max-h-96">
          <CardContent className="space-y-4">
            {workExperience.map((job, index) => (
              <div key={index} className="flex items-center gap-4">
                <img
                  src={job.logo}
                  alt={`${job.company} logo`}
                  className="w-12 h-12 object-contain rounded"
                  loading="lazy"
                />
                <div>
                  <div className="font-semibold">{job.company}</div>
                  <div className="text-sm text-muted-foreground">
                    {job.years}
                  </div>
                  <div className="text-sm">{job.title}</div>
                </div>
              </div>
            ))}
          </CardContent>
        </ScrollArea>
      </Card>
    </div>
  );
}
