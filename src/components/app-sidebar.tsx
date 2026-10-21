import * as React from "react";

import { DarkModeToggleButton } from "@/components/mode-toggle";
import { NavMain } from "@/components/nav-main";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Separator } from "@/components/ui/separator";
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenuButton,
  SidebarRail,
  SidebarTrigger,
} from "@/components/ui/sidebar";
import { sidebar } from "@/data/sidebar";

export function AppSidebar({ ...props }: React.ComponentProps<typeof Sidebar>) {
  return (
    <Sidebar collapsible="icon" {...props}>
      <SidebarHeader>
        <SidebarMenuButton
          tooltip="Toggle Sidebar"
          className="w-8 h-8 cursor-pointer"
          asChild
        >
          <SidebarTrigger />
        </SidebarMenuButton>

        <div className="flex flex-col w-full items-center justify-center gap-2 -mt-2 mb-3 group-data-[collapsible=icon]:mb-0">
          <Avatar className="w-24 h-24 group-data-[collapsible=icon]:w-0 group-data-[collapsible=icon]:h-0 transition-all duration-200">
            <AvatarImage src={sidebar.profileImage} />
            <AvatarFallback>PY</AvatarFallback>
          </Avatar>
          <span className="text-sm font-semibold group-data-[collapsible=icon]:hidden">
            {sidebar.userName}
          </span>
        </div>

        <Separator orientation="horizontal" />
      </SidebarHeader>
      <SidebarContent>
        <NavMain items={sidebar.sections} />
      </SidebarContent>
      <SidebarFooter>
        <DarkModeToggleButton />
      </SidebarFooter>
      <SidebarRail />
    </Sidebar>
  );
}
