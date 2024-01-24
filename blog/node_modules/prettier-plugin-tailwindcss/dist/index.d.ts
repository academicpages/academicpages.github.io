import { Parser, Printer, SupportOption } from 'prettier';

export interface PluginOptions {
  /**
   * Path to the Tailwind config file.
   */
  tailwindConfig?: string

  /**
   * List of custom function and tag names that contain classes.
   */
  tailwindFunctions?: string[]

  /**
   * List of custom attributes that contain classes.
   */
  tailwindAttributes?: string[]
}

declare module 'prettier' {
  interface RequiredOptions extends PluginOptions {}
  interface ParserOptions extends PluginOptions {}
}

export const options: Record<keyof PluginOptions, SupportOption>
export const parsers: Record<string, Parser>
export const printers: Record<string, Printer>
