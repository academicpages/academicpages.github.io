import { Link } from "react-router";
import { FaArrowRight } from "react-icons/fa6";
import { IoLibrary } from "react-icons/io5";

import { Button } from "@/components/ui/button";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

import { publicationsFeatured } from "@/data/publications.featured";

export default function PublicationsSection() {
  return (
    <div className="space-y-6">
      <div className="flex flex-row justify-center items-center gap-2 text-plus font-semibold">
        <IoLibrary />
        Publications
      </div>

      <div className="overflow-hidden">
        <Table className="table-fixed w-full">
          <TableHeader>
            <TableRow>
              <TableHead className="w-[calc(100%-50px)]">Publication</TableHead>
              <TableHead className="w-[46px] text-right">Year</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {publicationsFeatured.items.map((pub, index) => (
              <TableRow key={index} className="transition-none">
                <TableCell className="whitespace-normal space-y-1">
                  <a
                    href={pub.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-base text-base/4 font-semibold hover:underline underline-offset-4"
                  >
                    {pub.title}
                  </a>

                  <div className="text-sm leading-4.5 text-muted-foreground mt-1">
                    {pub.authors.split(", ").map((author, i) => (
                      <span
                        key={i}
                        className={
                          author === publicationsFeatured.authorName
                            ? "font-semibold"
                            : ""
                        }
                      >
                        {author}
                        {i < pub.authors.split(", ").length - 1 && ", "}
                      </span>
                    ))}
                  </div>

                  <div className="text-sm italic leading-4.5 text-muted-foreground">
                    {pub.venue}
                  </div>
                </TableCell>

                <TableCell className="text-sm text-right text-muted-foreground">
                  {pub.year}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>

      <div className="relative w-full">
        <div className="absolute right-0">
          <Button
            asChild
            variant="outline"
            size="sm"
            className="gap-1 text-muted-foreground"
          >
            <Link to="/publications">
              View all
              <FaArrowRight className="w-4 h-4" />
            </Link>
          </Button>
        </div>
      </div>
    </div>
  );
}
