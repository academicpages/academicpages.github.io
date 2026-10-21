import React from "react";
import { Sun, Moon } from "lucide-react";

import { useTheme } from "@/components/theme-provider";
import { Button } from "@/components/ui/button";
import { SidebarMenuButton } from "@/components/ui/sidebar";
import { cn } from "@/lib/utils";

export const DarkModeToggleButton = React.forwardRef<
  React.ComponentRef<typeof Button>,
  React.ComponentProps<typeof Button>
>(({ className, ...props }, ref) => {
  const { theme, setTheme } = useTheme();

  const toggleTheme = () => {
    setTheme(theme === "dark" ? "light" : "dark");
  };

  const tooltipMessage =
    theme === "dark" ? "Switch to Light Mode" : "Switch to Dark Mode";

  return (
    <SidebarMenuButton tooltip={tooltipMessage} asChild>
      <Button
        ref={ref}
        variant="ghost"
        size="icon"
        className={cn("cursor-pointer", className)}
        onClick={toggleTheme}
        {...props}
      >
        <div className="relative flex items-center justify-center h-[1.2rem] w-[1.2rem]">
          <Sun className="absolute h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
          <Moon className="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
        </div>
        <span className="group-data-[collapsible=icon]:hidden leading-tight">
          {theme === "dark" ? "Dark" : "Light"}
        </span>
      </Button>
    </SidebarMenuButton>
  );
});
