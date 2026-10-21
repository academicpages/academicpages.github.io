import { Outlet } from "react-router";

import { AppSidebar } from "@/components/app-sidebar";
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/components/ui/sidebar";
import { Button } from "@/components/ui/button";
import { Toaster } from "@/components/ui/sonner";

export default function Layout() {
  return (
    <SidebarProvider defaultOpen={false}>
      <AppSidebar variant="floating" />
      <SidebarInset className="min-h-screen">
        <SidebarTrigger className="fixed left-3 top-3 md:hidden z-5" />

        <div className="px-6 sm:px-12 py-24 grow">
          <Outlet />
        </div>

        {/* I would really appreciate it if you could keep the footer as it is to preserve attribution. Thank you! */}
        <footer className="text-sm w-full text-center border-t py-4">
          Created by
          <Button asChild variant="link" className="p-0 ml-1">
            <a
              href="https://github.com/pm25/showlit"
              target="_blank"
              rel="noopener noreferrer"
            >
              Showlit Template
            </a>
          </Button>
        </footer>

        <Toaster />
      </SidebarInset>
    </SidebarProvider>
  );
}
