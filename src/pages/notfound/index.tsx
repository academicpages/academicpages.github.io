import { Link } from "react-router";
import { FaArrowLeft } from "react-icons/fa6";

import { Button } from "@/components/ui/button";
import { usePageTitle } from "@/hooks/use-pagetitle";

export default function NotFoundPage() {
  usePageTitle("Page Not Found");

  return (
    <div className="flex flex-col items-center justify-center h-full space-y-4">
      <h1 className="text-4xl sm:text-5xl font-bold">404</h1>
      <p className="text-base sm:text-lg text-muted-foreground text-center">
        Oops! The page you're looking for doesn't exist.
      </p>
      <Button asChild variant="outline" className="mt-2 gap-1">
        <Link to="/">
          <FaArrowLeft className="w-4 h-4" /> Back to Home
        </Link>
      </Button>
    </div>
  );
}
