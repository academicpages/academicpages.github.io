declare module 'tailwind-bootstrap-grid' {
  import { PluginCreator } from "tailwindcss/types/config";

  interface GridGutters {
    [key: string]: string | number;
  }

  interface ContainerMaxWidths {
    [breakpoint: string]: string;
  }

  interface TailwindBootstrapGridOptions {
    gridColumns?: number;
    gridGutterWidth?: string;
    gridGutters?: GridGutters;
    generateContainer?: boolean;
    containerMaxWidths?: ContainerMaxWidths;
    rtl?: boolean;
    respectImportant?: boolean;
  }

  function tailwindBootstrapGrid(options?: TailwindBootstrapGridOptions): PluginCreator;
  export = tailwindBootstrapGrid;
}
