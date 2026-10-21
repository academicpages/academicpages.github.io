import { useLocation, Link } from "react-router";
import { ChevronLeft, type LucideIcon } from "lucide-react";
import type { IconType } from "react-icons";

import {
  SidebarGroup,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/components/ui/sidebar";

export function NavMain({
  items,
}: {
  items: {
    title: string;
    url: string;
    icon?: LucideIcon | IconType;
  }[];
}) {
  const location = useLocation();
  const normalizePath = (path: string) =>
    path.startsWith("/") ? path.slice(1) : path;
  const isActive = (url: string) =>
    normalizePath(location.pathname) === normalizePath(url);

  return (
    <SidebarGroup>
      <SidebarGroupLabel>Pages</SidebarGroupLabel>
      <SidebarMenu>
        {items.map((item) => (
          <SidebarMenuItem key={item.title}>
            <SidebarMenuButton tooltip={item.title} asChild>
              <Link to={item.url}>
                {item.icon && <item.icon />}
                <span>{item.title}</span>
                <ChevronLeft
                  className={`ml-auto transition-transform duration-200 ${
                    isActive(item.url) ? "rotate-0" : "rotate-180"
                  }`}
                />
              </Link>
            </SidebarMenuButton>
          </SidebarMenuItem>
        ))}
      </SidebarMenu>
    </SidebarGroup>
  );
}
