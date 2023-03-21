# What's New?

## 1.13.45
Bug Fixes:
- Remove unwanted warning "Configuration is already in progress" in multi-root projects. [#2989](https://github.com/microsoft/vscode-cmake-tools/issues/2989)
- `setKitByName` command ignores the workspace folder argument. [PR [#2991](https://github.com/microsoft/vscode-cmake-tools/issues/2991)](https://github.com/microsoft/vscode-cmake-tools/pull/2991)

## 1.13.44
Bug Fixes:
- Compatibility between test and build presets was not enforced. [#2904](https://github.com/microsoft/vscode-cmake-tools/issues/2904)
- Fix problems with updating the code model. [#2980](https://github.com/microsoft/vscode-cmake-tools/issues/2980)
- Validate presets in initialization. [#2976](https://github.com/microsoft/vscode-cmake-tools/issues/2976)

## 1.13.43
Bug Fixes:
- Fix an issue causing the Add Presets commands not to appear. [PR [#2977](https://github.com/microsoft/vscode-cmake-tools/issues/2977)](https://github.com/microsoft/vscode-cmake-tools/pull/2977)

## 1.13.42
Bug Fixes:
- Fix failed activation when using the `cmake.allowUnsupportedPresetsVersions` setting. [#2968](https://github.com/microsoft/vscode-cmake-tools/issues/2968)
- Verify binary directories only if there are multiple sources. [#2963](https://github.com/microsoft/vscode-cmake-tools/issues/2963)
- Update quote function to fix path separator regression [#2974](https://github.com/microsoft/vscode-cmake-tools/pull/2974)

## 1.13.41
Bug Fixes:
- Fix "No folder is open" error when running quick start. [#2951](https://github.com/microsoft/vscode-cmake-tools/issues/2951)
- Add a control statement to the 'quote' function in shlex.ts to return the string without quotes. [#2955]
(https://github.com/microsoft/vscode-cmake-tools/issues/2955)
- CMake Tools fails to initialize the Active Project. [#2952](https://github.com/microsoft/vscode-cmake-tools/issues/2952)

## 1.13.40
Improvements:
- Support multiple projects in a single workspace folder. `cmake.sourceDirectory` setting now allows setting multiple paths. [#1374](https://github.com/microsoft/vscode-cmake-tools/issues/1374)
- Add a setting to disable reading `compile_commands.json`. [#2586](https://github.com/microsoft/vscode-cmake-tools/issues/2586) [@xiaoyun94](https://github.com/xiaoyun94)
- Preset in CMakeUserPresets.json using "condition" does not appear in configure preset selection. [#2749](https://github.com/microsoft/vscode-cmake-tools/issues/2749)
- Resolve workspace variables in `cmake-kits.json`. [#2737](https://github.com/microsoft/vscode-cmake-tools/issues/2737)
- Use upper case drive letters on Windows for `cmake.sourceDirectory`. [PR [#2665](https://github.com/microsoft/vscode-cmake-tools/issues/2665)](https://github.com/microsoft/vscode-cmake-tools/pull/2665) [@Danielmelody](https://github.com/Danielmelody)
- Custom browse configuration should not include (redundant) per-file arguments. [#2645](https://github.com/microsoft/vscode-cmake-tools/issues/2645)
- Support optional generator in `configurePresets` for version 3 and higher. [#2734](https://github.com/microsoft/vscode-cmake-tools/issues/2734) [@jochil](https://github.com/jochil)
- Add a public API for extension authors that depend on CMake Tools. [#494](https://github.com/microsoft/vscode-cmake-tools/issues/494)
- Support explicit typing in `cmake.configureSettings`. [#1457](https://github.com/microsoft/vscode-cmake-tools/issues/1457)
- Scan for kits will now add ARM64 hosts for MSVC. [PR [#2887](https://github.com/microsoft/vscode-cmake-tools/issues/2887)](https://github.com/microsoft/vscode-cmake-tools/pull/2887) [@scaryrawr](https://github.com/scaryrawr)
- Support canceling configuration [#2436](https://github.com/microsoft/vscode-cmake-tools/issues/2436) [@Danielmelody](https://github.com/Danielmelody)
- Pop up "Choose CMakeLists.txt" when user goes to configure while feature set is partially activated. [#2746](https://github.com/microsoft/vscode-cmake-tools/issues/2746)
- Adhere to the setting entry "Parallel Jobs" (`cmake.parallelJobs`) when generating the default build preset. [#2765](https://github.com/microsoft/vscode-cmake-tools/issues/2765) [@maxmitti](https://github.com/maxmitti)
- Add a setting to ignore unknown presets features from the versions that CMake Tools doesn't support yet. [#1963](https://github.com/microsoft/vscode-cmake-tools/issues/1963)

Bug Fixes:
- Fix warning message that appears when using a default build preset with a multi-config generator. [#2353](https://github.com/microsoft/vscode-cmake-tools/issues/2353)
- Update kits documentation. [#2761](https://github.com/microsoft/vscode-cmake-tools/issues/2761) [@jdeaton](https://github.com/jdeaton)
- Avoid calling build tasks for "Clean", "Install" and "Run Tests" commands when "cmake: buildTask" setting is true. [#2768](https://github.com/microsoft/vscode-cmake-tools/issues/2768)
- Generate the correct `configurePresets` for Clang or GCC compilers on Windows. [#2733](https://github.com/microsoft/vscode-cmake-tools/issues/2773)
- CMake Tools does not send `--target=` to cpptools. [#1896](https://github.com/microsoft/vscode-cmake-tools/issues/1896) [#2800](https://github.com/microsoft/vscode-cmake-tools/issues/2800)
- Fix the build task to return the error code. [#2799](https://github.com/microsoft/vscode-cmake-tools/issues/2799) [@BIKA-C](https://github.com/BIKA-C)
- Generate correct ClangCL Kits. [#2790](https://github.com/microsoft/vscode-cmake-tools/issues/2790) [#2810](https://github.com/microsoft/vscode-cmake-tools/issues/2810)
- Cache the version check for the cmake executable. [#2818](https://github.com/microsoft/vscode-cmake-tools/issues/2818)
- ctest -N does not work with custom cmake path from preset. [#2842](https://github.com/microsoft/vscode-cmake-tools/issues/2842)
- Resolve variables in args before passing them to the terminal. [#2846](https://github.com/microsoft/vscode-cmake-tools/issues/2846)
- Quote launch arguments sent to the terminal if they have special characters. [#2898](https://github.com/microsoft/vscode-cmake-tools/issues/2898)
- CMake Tools should choose cmake.exe from the newest VS when it's not found in the PATH. [#2753](https://github.com/microsoft/vscode-cmake-tools/issues/2753)
- Calling build targets from CMake Project Outline always builds default target if useTasks option is set. [#2778](https://github.com/microsoft/vscode-cmake-tools/issues/2768) [@piomis](https://github.com/piomis)
- Fix `${command:cmake.buildType}` so that it returns the right value when using CMake Presets. [#2894](https://github.com/microsoft/vscode-cmake-tools/issues/2894)
- Fix a problem with multi-root projects not activating the configuration provider. [#2915](https://github.com/microsoft/vscode-cmake-tools/issues/2915)
- Remove the default path for `cmake.mingwSearchDirs` since the path is world-writable. [PR [#2942](https://github.com/microsoft/vscode-cmake-tools/issues/2942)](https://github.com/microsoft/vscode-cmake-tools/pull/2942)
- Build command is not able to properly pick-up tasks from tasks.json file if configured with isDefault option and cancellation of running build task is not working. [#2935](https://github.com/microsoft/vscode-cmake-tools/issues/2935) [@piomis](https://github.com/piomis)

## 1.12.27
Bug Fixes:
- Add default target to the build task when target is not defined. [#2729](https://github.com/microsoft/vscode-cmake-tools/issues/2729)

## 1.12.26
Improvements:
- Support for presets version 4. [#2492](https://github.com/microsoft/vscode-cmake-tools/issues/2492) [@chausner](https://github.com/chausner)
- Triggering reconfigure after changes are made to included files. [#2526](https://github.com/microsoft/vscode-cmake-tools/issues/2526) [@chausner](https://github.com/chausner)
- Add target name to terminal window name for launch. [#2613](https://github.com/microsoft/vscode-cmake-tools/issues/2613)
- Add support for "preset" and "env" in task provider. [#2636](https://github.com/microsoft/vscode-cmake-tools/issues/2636) [#2553](https://github.com/microsoft/vscode-cmake-tools/issues/2553) [#2714](https://github.com/microsoft/vscode-cmake-tools/issues/2714) [#2706](https://github.com/microsoft/vscode-cmake-tools/issues/2706)
- Add Craig Scott's "Professional CMake" book to the list of resources in doc/faq.md for learning CMake. [#2679](https://github.com/microsoft/vscode-cmake-tools/pull/2679) [@david-fong](https://github.com/david-fong)

Bug Fixes:
- CMakeUserPresets.json version not detected without CMakePresets.json. [#2469](https://github.com/microsoft/vscode-cmake-tools/issues/2469) [@chausner](https://github.com/chausner)
- Do not prompt to select a Kit if `cmake.configureOnOpen` is `false`. [#2538](https://github.com/microsoft/vscode-cmake-tools/issues/2538)
- Don't delete CMakeCache.txt when switching kits if the buildDirectory also changes. [#2546](https://github.com/microsoft/vscode-cmake-tools/issues/2546) [@david-fong](https://github.com/david-fong)
- Set the working directory for the file api driver. [#2569](https://github.com/microsoft/vscode-cmake-tools/issues/2569)
- Add "description" properties to the cmake.revealLog setting. [#2578](https://github.com/microsoft/vscode-cmake-tools/issues/2578)
- Detect clang-cl.exe compilers that are not bundled with Visual Studio. [#2622](https://github.com/microsoft/vscode-cmake-tools/issues/2622)
- Clear output channel after auto-reconfigure. [#2628](https://github.com/microsoft/vscode-cmake-tools/issues/2628)
- Fix issues with launching the target in PowerShell terminal. [#2650](https://github.com/microsoft/vscode-cmake-tools/issues/2650) [#2621](https://github.com/microsoft/vscode-cmake-tools/issues/2621) [#535](https://github.com/microsoft/vscode-cmake-tools/issues/535)
- Respect VS Code setting "insertSpaces" when updating preset files via GUI. [#2677](https://github.com/microsoft/vscode-cmake-tools/issues/2677)
- CMake install task does not run in terminal. [#2693](https://github.com/microsoft/vscode-cmake-tools/issues/2693)
- Deprecation warnings show up as errors in Problems view. [#2708](https://github.com/microsoft/vscode-cmake-tools/issues/2708)

## 1.11.26
- Revert back to the previous CMake language server extension dependency. [PR [#2599](https://github.com/microsoft/vscode-cmake-tools/issues/2599)](https://github.com/microsoft/vscode-cmake-tools/pull/2599)

Bug Fixes:
- Ninja is used as a default generator. [#2598](https://github.com/microsoft/vscode-cmake-tools/issues/2598) 

## 1.11.25
Improvements:
- Fix build Error: EMFILE: too many open files. [#2288](https://github.com/microsoft/vscode-cmake-tools/issues/2288) [@FrogTheFrog](https://github.com/FrogTheFrog)
- Add commands to get preset names. [PR [#2433](https://github.com/microsoft/vscode-cmake-tools/issues/2433)](https://github.com/microsoft/vscode-cmake-tools/pull/2433)
- Add IntelliSense support for `debugConfig.console`. [#2428](https://github.com/microsoft/vscode-cmake-tools/issues/2428)
- Add c++23 support. [#2475](https://github.com/microsoft/vscode-cmake-tools/issues/2475) [@sweemer](https://github.com/sweemer)
- Add support for multiple targets in the CMake task provider. [#2122](https://github.com/microsoft/vscode-cmake-tools/issues/2122)
- Add setting `cmake.showSystemKits`. [PR [#2520](https://github.com/microsoft/vscode-cmake-tools/issues/2520)](https://github.com/microsoft/vscode-cmake-tools/pull/2520) [@bharatvaj](https://github.com/bharatvaj)
- Add support for "Configure", "Install" and "Test" tasks. [#2452](https://github.com/microsoft/vscode-cmake-tools/issues/2452)
- Add setting `cmake.ignoreCMakeListsMissing`. [PR [#2537](https://github.com/microsoft/vscode-cmake-tools/issues/2537)](https://github.com/microsoft/vscode-cmake-tools/pull/2537) [@ilg-ul](https://github.com/ilg-ul)
- Add support for "Clean" and "Clean Rebuild" tasks. [#2555](https://github.com/microsoft/vscode-cmake-tools/issues/2555)
- The extension for CMake language support is replaced. [PR [#2267](https://github.com/microsoft/vscode-cmake-tools/issues/2267)](https://github.com/microsoft/vscode-cmake-tools/pull/2267) [@josetr](https://github.com/josetr)

Bug Fixes:
- `Clean All Projects` menu item builds rather than cleans. [#2460](https://github.com/microsoft/vscode-cmake-tools/issues/2460)
- Update terminal's environment variables when the kit is changed. [#2364](https://github.com/microsoft/vscode-cmake-tools/issues/2364)
- Add timeouts for compiler scanning. [#1289](https://github.com/microsoft/vscode-cmake-tools/issues/1289)
- Fix schema validation for presets version 4. [#2490](https://github.com/microsoft/vscode-cmake-tools/issues/2490)
- Remove problematic environment variables from the debugger environment. [#2442](https://github.com/microsoft/vscode-cmake-tools/issues/2442)
- Fix preferredGenerator "Watcom WMake" not working. [#2500](https://github.com/microsoft/vscode-cmake-tools/issues/2500)
- When `debugConfig` has specific modes or debugger paths set, the linker check heuristic should be skipped. [#2509](https://github.com/microsoft/vscode-cmake-tools/issues/2509)
- Exclude environment variables from debugging if the values have newlines. [#2515](https://github.com/microsoft/vscode-cmake-tools/issues/2515)
- Correctly configure the build environment when using VS 2015 and Ninja in CMakePresets.json. [#2516](https://github.com/microsoft/vscode-cmake-tools/issues/2516)
- Select the correct VS toolset for Ninja generators with CMake Presets. [#2423](https://github.com/microsoft/vscode-cmake-tools/issues/2423)
- Fix unhandled exception with CMakePresets.json. [#2117](https://github.com/microsoft/vscode-cmake-tools/issues/2117)
- Fix issues with compiler argument quoting when configuring IntelliSense. [#2563](https://github.com/microsoft/vscode-cmake-tools/pull/2563)
- Fix clang version detection regexes. [PR [#2549](https://github.com/microsoft/vscode-cmake-tools/issues/2549)](https://github.com/microsoft/vscode-cmake-tools/pull/2549) [@chausner](https://github.com/chausner)

## 1.10.5
Bug Fixes:
- fix "CMake: compile active file" command. [#2438](https://github.com/microsoft/vscode-cmake-tools/issues/2438)

## 1.10.4
Improvements:
- Don't specify number of jobs when building with Ninja. [#696](https://github.com/microsoft/vscode-cmake-tools/issues/696)
- Support for the Ninja Multi-Config generator. [#1423](https://github.com/microsoft/vscode-cmake-tools/issues/1423)
- Minimize build progress notification to the status bar. [#2308](https://github.com/microsoft/vscode-cmake-tools/issues/2308)
- Allow editing Kits when presets are in use. [#1965](https://github.com/microsoft/vscode-cmake-tools/issues/1965)
- Launch the target in the default terminal. [PR [#2311](https://github.com/microsoft/vscode-cmake-tools/issues/2311)](https://github.com/microsoft/vscode-cmake-tools/pull/2311) [@michallukowski](https://github.com/michallukowski)
- Allow launching targets in parallel. [#2240](https://github.com/microsoft/vscode-cmake-tools/issues/2120) [@ColinDuquesnoy](https://github.com/ColinDuquesnoy)

Bug Fixes:
- CMakePrests.json toolset requires the VS version instead of the toolset version. [#1965](https://github.com/microsoft/vscode-cmake-tools/issues/1965)
- CMakePresets should be able to specify a VC toolset by version number. [#2366](https://github.com/microsoft/vscode-cmake-tools/pull/2366)
- CMake task provider does not configure the VS Build environment for Ninja builds. [#2258](https://github.com/microsoft/vscode-cmake-tools/pull/2258)
- `${buildKit}` is not updated after a Kit switch. [#2335](https://github.com/microsoft/vscode-cmake-tools/issues/2335)
- Test the existence of a property instead of the value when expanding preset conditions. [#2329](https://github.com/microsoft/vscode-cmake-tools/issues/2329)
- Include `hostSystemName` in variable expansion when only using User presets. [#2362](https://github.com/microsoft/vscode-cmake-tools/issues/2362)
- Trim whitespace from `environmentSetupScript`. [#2391](https://github.com/microsoft/vscode-cmake-tools/issues/2391)
- Incorrect `cmake.additionalKits` setting breaks CMake extension. [#2382](https://github.com/microsoft/vscode-cmake-tools/issues/2382)
- VS2010 compile errors are not shown in Problems. [#2376](https://github.com/microsoft/vscode-cmake-tools/issues/2376)
- Always rebuilds sources with autodetected clang and ninja on linux. [#2289](https://github.com/microsoft/vscode-cmake-tools/issues/2289)
- Clean Reconfigure All Projects removes wrong files after switching kit. [#2326](https://github.com/microsoft/vscode-cmake-tools/issues/2326)
- Update documentation. [#2334](https://github.com/microsoft/vscode-cmake-tools/pull/2334) [@atsju](https://github.com/atsju)
- Ninja not able to build single-threaded. [#2222](https://github.com/microsoft/vscode-cmake-tools/issues/2222)
- Fix various kit detection issues. [#2246](https://github.com/microsoft/vscode-cmake-tools/issues/2246) [#1759](https://github.com/microsoft/vscode-cmake-tools/issues/1759) [#1653](https://github.com/microsoft/vscode-cmake-tools/issues/1653) [#1410](https://github.com/microsoft/vscode-cmake-tools/issues/1410) [#1233](https://github.com/microsoft/vscode-cmake-tools/issues/1233) [@fourdim](https://github.com/fourdim)
- Stop using `-H` to configure projects. [#2292](https://github.com/microsoft/vscode-cmake-tools/issues/2292)
- `environmentSetupScript` capitalizes environment variable names. [#1592](https://github.com/microsoft/vscode-cmake-tools/issues/1592) [@lygstate](https://github.com/lygstate)
- Debug Target failed when `debugConfig.environment` not present. [#2236](https://github.com/microsoft/vscode-cmake-tools/issues/2236) [@lygstate](https://github.com/lygstate)
- Presets in CMakePresets.json should not inherit from presets in CMakeUserPresets.json. [#2232](https://github.com/microsoft/vscode-cmake-tools/issues/2232)
- Refresh the launch terminal if the user default changes. [PR [#2408](https://github.com/microsoft/vscode-cmake-tools/issues/2408)](https://github.com/microsoft/vscode-cmake-tools/pull/2408)
- Strip BOM from files when reading. [#2396](https://github.com/microsoft/vscode-cmake-tools/issues/2396)
- When using the configuration provider for the C++ extension, the browse configuration was not being updated after code model changes. [#2410](https://github.com/microsoft/vscode-cmake-tools/issues/2410)

## 1.9.2
Bug fixes:
- Fix infinite recursion into symlinks. [#2257](https://github.com/microsoft/vscode-cmake-tools/issues/2257)
- Fix `Show Build Command` for folders that do not use CMake Presets. [#2211](https://github.com/microsoft/vscode-cmake-tools/issues/2211)
- Fix presets not shown when a common dependency is inherited more than once. [#2210](https://github.com/microsoft/vscode-cmake-tools/issues/2210)
- Fix IntelliSense usage of short name from variants file for buildType. [#2120](https://github.com/microsoft/vscode-cmake-tools/issues/2120) [@gost-serb](https://github.com/gost-serb)

## 1.9.1
Bug fixes:
- Fix presets using conditions with macros and inheritance. [#2185](https://github.com/microsoft/vscode-cmake-tools/issues/2185)
- Parallelism no longer working in 1.9.0 for CMake < 3.14.0. [#2181](https://github.com/microsoft/vscode-cmake-tools/issues/2181)
- `CMake: Compile Active File` command stopped working in v1.9.0. [#2180](https://github.com/microsoft/vscode-cmake-tools/issues/2180)
- Exception after successful build when cpptools IntelliSense is disabled. [#2188](https://github.com/microsoft/vscode-cmake-tools/issues/2188)
- Fix issue with presets (v3) and "toolchainFile". [#2179](https://github.com/microsoft/vscode-cmake-tools/issues/2179)
- Don't add `-j` argument when `cmake.parallelJobs` is set to `1`. [#1958](https://github.com/microsoft/vscode-cmake-tools/issues/1958) [@mark-ulrich](https://github.com/mark-ulrich)
- Warn the user about CMAKE_BUILD_TYPE inconsistencies. [#2096](https://github.com/microsoft/vscode-cmake-tools/issues/2096)

## 1.9.0
Improvements:
- Add support for CMakePresets version 3. [#1904](https://github.com/microsoft/vscode-cmake-tools/issues/1904)
- Add diagnostic support for parsing IAR compiler output. [PR [#2131](https://github.com/microsoft/vscode-cmake-tools/issues/2131)](https://github.com/microsoft/vscode-cmake-tools/pull/2131) [@willson556](https://github.com/willson556)
- Add "Log Diagnostics" command. [PR [#2141](https://github.com/microsoft/vscode-cmake-tools/issues/2141)](https://github.com/microsoft/vscode-cmake-tools/pull/2141)
- Add build and configure commands to show cmake commands without running them. [PR [#1767](https://github.com/microsoft/vscode-cmake-tools/issues/1767)](https://github.com/microsoft/vscode-cmake-tools/pull/1767)
- Implement support for merging multiple compile_commands in super-builds sub-folders of the build directory. [PR [#2029](https://github.com/microsoft/vscode-cmake-tools/issues/2029)](https://github.com/microsoft/vscode-cmake-tools/pull/2029) [@Felix-El](https://github.com/Felix-El)
- Add `cmake.allowCommentsInPresetsFile` setting to allow JS style comments in CMakePresets files. [#2169](https://github.com/microsoft/vscode-cmake-tools/issues/2169)

Bug fixes:
- MSVC_VERSION is incorrect when cmake configures with clang-cl. [#1053](https://github.com/microsoft/vscode-cmake-tools/issues/1053) [@tklajnscek](https://github.com/tklajnscek)
- Build error because `binaryDir` removed after configure. [#2128](https://github.com/microsoft/vscode-cmake-tools/issues/2128)
- Configuration from build presets ignored by Intellisense and launch (when using multi config generators). [#2099](https://github.com/microsoft/vscode-cmake-tools/issues/2099)
- Extra {0} output message when having preset with circular inherits. [#2118](https://github.com/microsoft/vscode-cmake-tools/issues/2118)
- CMake-Tools does not reconfigure after a change of CMakeLists.txt in a subdirectory of root. [#1911](https://github.com/microsoft/vscode-cmake-tools/issues/1911) [@AbdullahAmrSobh](https://github.com/AbdullahAmrSobh)
- Fixes msvc2015 detection when only vs2019 are installed. [#1955](https://github.com/microsoft/vscode-cmake-tools/issues/1955) [@lygstate](https://github.com/lygstate)
- Allow for clang compilers to be set in presets without full path. [#1922](https://github.com/microsoft/vscode-cmake-tools/issues/1922)
- Compiler flags containing spaces not passed correctly to IntelliSense. [#1414](https://github.com/microsoft/vscode-cmake-tools/issues/1414)
- Don't scan the whole workspace for CMakeLists.txt, just a few folders. [#2127](https://github.com/microsoft/vscode-cmake-tools/issues/2127)
- Regression with Visual Studio generator and non-default toolset. [#2147](https://github.com/microsoft/vscode-cmake-tools/issues/2147)
- Debug shows "No compiler found in cache file." dialog. [#2121](https://github.com/microsoft/vscode-cmake-tools/issues/2121)
- Unable to work with pre-configured projects (cache is deleted). [#2140](https://github.com/microsoft/vscode-cmake-tools/issues/2140)
- Unknown C/C++ standard control flags: -std=gnu++2b and -std=c2x. [#2150](https://github.com/microsoft/vscode-cmake-tools/issues/2150)
- Select the most recently used build/test preset when configure preset changes. [#1927](https://github.com/microsoft/vscode-cmake-tools/issues/1927)
- Re-enable build target selection when using presets. [#1872](https://github.com/microsoft/vscode-cmake-tools/issues/1872)

## 1.8.1
Bug fixes:
- Command substitutions in launch.json are broken. [#2091](https://github.com/microsoft/vscode-cmake-tools/issues/2091)
- `cmake.configureOnOpen` setting is ignored. [#2088](https://github.com/microsoft/vscode-cmake-tools/issues/2088)
- User-defined preset not shown when inheriting from `CMakePresets.json`. [#2082](https://github.com/microsoft/vscode-cmake-tools/issues/2082)
- Fix presets using server API. [#2026](https://github.com/microsoft/vscode-cmake-tools/issues/2026)

## 1.8.0
Improvements:
- Last selected target isn't read on start up. [#1148](https://github.com/microsoft/vscode-cmake-tools/issues/1148)
- Use cached cmake-file-api response to configure IntelliSense on startup. [#1149](https://github.com/microsoft/vscode-cmake-tools/issues/1149)
- Show a quickPick of all the CMakeLists.txt inside the project (if none exists where "cmake.sourceDirectory" points at). [#533](https://github.com/microsoft/vscode-cmake-tools/issues/533)
- Add command to get the active folder of a workspace. [#1715](https://github.com/microsoft/vscode-cmake-tools/issues/1715) [@guestieng](https://github.com/guestieng)
- Task provider refactoring to best utilize latest updates from VSCode. [PR [#1880](https://github.com/microsoft/vscode-cmake-tools/issues/1880)](https://github.com/microsoft/vscode-cmake-tools/pull/1880)
- Add docker container definition. [PR [#1758](https://github.com/microsoft/vscode-cmake-tools/issues/1758)](https://github.com/microsoft/vscode-cmake-tools/pull/1758)
- Enhance the vsix build with package scripts in package.json. [PR [#1752](https://github.com/microsoft/vscode-cmake-tools/issues/1752)](https://github.com/microsoft/vscode-cmake-tools/pull/1752) [@lygstate](https://github.com/lygstate)

Bug fixes:
- Fix various presets field settings to be passed correctly on to CMake. [#2009](https://github.com/microsoft/vscode-cmake-tools/issues/2009)
- Check for target architecture when reading toolchain FileAPI. [#1879](https://github.com/microsoft/vscode-cmake-tools/issues/1879)
- Fix environment variable in debugging docs. [PR [#1874](https://github.com/microsoft/vscode-cmake-tools/issues/1874)](https://github.com/microsoft/vscode-cmake-tools/pull/1874) [@zariiii9003](https://github.com/zariiii9003)
- Fix typo in variant docs. [PR [#1970](https://github.com/microsoft/vscode-cmake-tools/issues/1970)](https://github.com/microsoft/vscode-cmake-tools/pull/1970) [@melak47](https://github.com/melak47)
- Update schema for preset cache variable CMAKE_BUILD_TYPE. [#1934](https://github.com/microsoft/vscode-cmake-tools/issues/1934)
- Fix regression in ctestDefaultArgs (ctest hardcoded directives: -T, test, --output-on-failure). [#1956](https://github.com/microsoft/vscode-cmake-tools/issues/1956)
- Don't throw when unknown diagnostics apepar. [#1796](https://github.com/microsoft/vscode-cmake-tools/issues/1796)
- Add parse target triple to fix "bad clang binary" error. [#1916](https://github.com/microsoft/vscode-cmake-tools/issues/1916) [@lygstate](https://github.com/lygstate)
- Include CMAKE_BUILD_TYPE in the generated text of configure preset. [#1847](https://github.com/microsoft/vscode-cmake-tools/issues/1847)
- Show also the "hidden" presets in the "Inherit from configure presets" quick pick. [#1923](https://github.com/microsoft/vscode-cmake-tools/issues/1923)
- Clang-cl diagnostics don't appear in Problems view. [#517](https://github.com/microsoft/vscode-cmake-tools/issues/517) [@ki-bo](https://github.com/ki-bo)
- Fix duplication in name of MSVC versus LLVM Clang kit. [PR [#1951](https://github.com/microsoft/vscode-cmake-tools/issues/1951)](https://github.com/microsoft/vscode-cmake-tools/pull/1951) [@lygstate](https://github.com/lygstate)
- Fixes output encoding in the vcvars setup process. [PR [#1985](https://github.com/microsoft/vscode-cmake-tools/issues/1985)](https://github.com/microsoft/vscode-cmake-tools/pull/1985) [@lygstate](https://github.com/lygstate)
- Remove vendor support since the string expansion is wrong for it. [#1966](https://github.com/microsoft/vscode-cmake-tools/issues/1966)
- Add configure preset environment to debug/launch. [#1884](https://github.com/microsoft/vscode-cmake-tools/issues/1884)
- Fix msvc2015 detection when only vs2019 is installed. [#1905](https://github.com/microsoft/vscode-cmake-tools/issues/1905) [@lygstate](https://github.com/lygstate)
- Prevent file index overwritting in multi-config generators. [#1800](https://github.com/microsoft/vscode-cmake-tools/issues/1800) [@andredsm](https://github.com/andredsm)
- Various cache variables edit/save fixes. [PR [#1826](https://github.com/microsoft/vscode-cmake-tools/issues/1826)](https://github.com/microsoft/vscode-cmake-tools/pull/1826) [@aemseemann](https://github.com/aemseemann)
- Use JSON as the language mode of preset files. [#2035](https://github.com/microsoft/vscode-cmake-tools/issues/2035)
- Fix broken links to contributing file. [PR [#2016](https://github.com/microsoft/vscode-cmake-tools/issues/2016)](https://github.com/microsoft/vscode-cmake-tools/pull/2016) [@andredsm](https://github.com/andredsm)
- Kit scan generates incorrect kits for VS 2022 [#2054](https://github.com/microsoft/vscode-cmake-tools/issues/2054)
- Fix presets for msvc compilers with x86 outputs [PR [#2072](https://github.com/microsoft/vscode-cmake-tools/issues/2072)](https://github.com/microsoft/vscode-cmake-tools/pull/2072)

## 1.7.3
Bug fixes:
- Make sure CMake Tools configuration provider gets registered with presets on. [#1832](https://github.com/microsoft/vscode-cmake-tools/issues/1832)
- Add the license field to package.json. [#1823](https://github.com/microsoft/vscode-cmake-tools/issues/1823)
- Add title to "Select target" quickpick. [#1860](https://github.com/microsoft/vscode-cmake-tools/issues/1860)

## 1.7.2
Bug fixes:
- Fix paths of target sources outside the workspace. [#1504](https://github.com/microsoft/vscode-cmake-tools/issues/1504) [@sleiner](https://github.com/sleiner)
- Use stricter type checks in presets expansion. [#1815](https://github.com/microsoft/vscode-cmake-tools/issues/1815)
- Solve conflict between -DCMAKE_GENERAOR:STRING=Ninja versus -G "Visual Studio 16 2019" -A x64. [PR [#1753](https://github.com/microsoft/vscode-cmake-tools/issues/1753)](https://github.com/microsoft/vscode-cmake-tools/pull/1753) [@lygstate](https://github.com/lygstate)
- Fix operator precedence when getting code page. [#1615](https://github.com/microsoft/vscode-cmake-tools/issues/1615) [@taoyouh](https://github.com/taoyouh)
- Override the locale when querying compiler versions. [#1821](https://github.com/microsoft/vscode-cmake-tools/issues/1821)
- Fix typo in CMakePresets.json schema. [PR [#1809](https://github.com/microsoft/vscode-cmake-tools/issues/1809)](https://github.com/microsoft/vscode-cmake-tools/pull/1809) [@bluec0re](https://github.com/bluec0re)


## 1.7.1
Improvements:
- CppTools-API v5 integration. [#1624](https://github.com/microsoft/vscode-cmake-tools/issues/1624)

Bug fixes:
- Correct macros evaluation in inherited presets. [#1787](https://github.com/microsoft/vscode-cmake-tools/issues/1787)
- Macro expansions should consider environment variables defined in the kit. [#1250](https://github.com/microsoft/vscode-cmake-tools/issues/1250)
- Fix 1.7.0 IntelliSense regression related to default standard and CppTools provider version. [#1788](https://github.com/microsoft/vscode-cmake-tools/issues/1788)
- Correct folder information for presets in multi-root projects. [PR [#1785](https://github.com/microsoft/vscode-cmake-tools/issues/1785)](https://github.com/microsoft/vscode-cmake-tools/pull/1785)


## 1.7.0
Improvements:
- Support for CMake Presets. [#529](https://github.com/microsoft/vscode-cmake-tools/issues/529)
- Support for File API "toolchains" object.
- User defined additional kits. [PR [#1701](https://github.com/microsoft/vscode-cmake-tools/issues/1701)](https://github.com/microsoft/vscode-cmake-tools/pull/1701) [@mjvankampen](https://github.com/mjvankampen)
- Touchbar extra functionality. [PR [#1693](https://github.com/microsoft/vscode-cmake-tools/issues/1693)](https://github.com/microsoft/vscode-cmake-tools/pull/1693) [@poterba](https://github.com/poterba)

Bug fixes:
- Can not compile active file if definition has quoted text. [#969](https://github.com/microsoft/vscode-cmake-tools/issues/969)
- Compiler flags containing spaces not passed correctly to IntelliSense. [#1414](https://github.com/microsoft/vscode-cmake-tools/issues/1414)
- Gcc/clang version analysis improvements. [#1575](https://github.com/microsoft/vscode-cmake-tools/issues/1575)
- Disable the extension when no CMakeLists is present. [#1578](https://github.com/microsoft/vscode-cmake-tools/issues/1578)
- Remove the "CMake Tools initializing" popup message. [#1518](https://github.com/microsoft/vscode-cmake-tools/issues/1518)
- Allow CppTools to chose a C/Cpp standard default. [#1477](https://github.com/microsoft/vscode-cmake-tools/issues/1477)
- Added ${workspaceHash} variable. [PR [#1055](https://github.com/microsoft/vscode-cmake-tools/issues/1055)](https://github.com/microsoft/vscode-cmake-tools/pull/1055) [@Zingam](https://github.com/Zingam)
- Setup CMT_MINGW_PATH properly on win32. [PR [#1611](https://github.com/microsoft/vscode-cmake-tools/issues/1611)](https://github.com/microsoft/vscode-cmake-tools/pull/1611) [@lygstate](https://github.com/lygstate)
- Codespaces specific changes of configureOnOpen default and popup UI. [#1676](https://github.com/microsoft/vscode-cmake-tools/issues/1676)
- Fixes environment expanding and document testEnvironment. [PR [#1598](https://github.com/microsoft/vscode-cmake-tools/issues/1598)](https://github.com/microsoft/vscode-cmake-tools/pull/1598) [@lygstate](https://github.com/lygstate)
- Pass cmake.debugConfig.args to launch target. [PR [#1603](https://github.com/microsoft/vscode-cmake-tools/issues/1603)](https://github.com/microsoft/vscode-cmake-tools/pull/1603) [@jbdamiano](https://github.com/jbdamiano)
- Dependencies package versions upgrade. [PR [#1475](https://github.com/microsoft/vscode-cmake-tools/issues/1475)](https://github.com/microsoft/vscode-cmake-tools/pull/1475) [@lygstate](https://github.com/lygstate)
- Add vendor hostOs targetOs targetArch versionMajor versionMinor attributes for kit. [PR [#1337](https://github.com/microsoft/vscode-cmake-tools/issues/1337)](https://github.com/microsoft/vscode-cmake-tools/pull/1337) [@lygstate](https://github.com/lygstate)
- Always correctly build target executable path. [PR [#1674](https://github.com/microsoft/vscode-cmake-tools/issues/1674)](https://github.com/microsoft/vscode-cmake-tools/pull/1674) [@falbrechtskirchinger](https://github.com/falbrechtskirchinger)
- Use variables instead of hardcoded values for system path references. [#883](https://github.com/microsoft/vscode-cmake-tools/issues/883) [@Zingam](https://github.com/Zingam)
- ctestPath should allow the same substitutions as cmakePath. [#785](https://github.com/microsoft/vscode-cmake-tools/issues/785) [@FakeTruth](https://github.com/FakeTruth)
- Change the order of available kits such that folder kits come first. [#1736](https://github.com/microsoft/vscode-cmake-tools/issues/1736)
- Fix "Configuring project" infinite loop when using "Locate" on a project without CMakeLists.txt. [#1704](https://github.com/microsoft/vscode-cmake-tools/issues/1704)
- Fix problems with using gdb debugger on MAC. [#1691](https://github.com/microsoft/vscode-cmake-tools/issues/1691)
- Fix parsing of target architecture flags with values that include arm64. [#1735](https://github.com/microsoft/vscode-cmake-tools/issues/1735)
- Changed ctest --output-on-failure from hardcode to default argument. [PR [#1729](https://github.com/microsoft/vscode-cmake-tools/issues/1729)](https://github.com/microsoft/vscode-cmake-tools/pull/1729) [@PedroLima92](https://github.com/PedroLima92)
- Update cmake-settings.md document. [PR [#1754](https://github.com/microsoft/vscode-cmake-tools/issues/1754)](https://github.com/microsoft/vscode-cmake-tools/pull/1754) [@lygstate](https://github.com/lygstate)


## 1.6.0
Bug Fixes:
- Fix Clang kit detection when version is at end of line. [#1342](https://github.com/microsoft/vscode-cmake-tools/issues/1342) [@falbrechtskirchinger](https://github.com/falbrechtskirchinger)
- Fix cache variables regular expression dealing with '='. [#1613](https://github.com/microsoft/vscode-cmake-tools/issues/1613)
- Add cmake.exportCompileCommandFile. [#1440](https://github.com/microsoft/vscode-cmake-tools/issues/1440)
- Fix the regexp of Gcc/Clang version to account for localization and more possible text patterns. [#1575](https://github.com/microsoft/vscode-cmake-tools/issues/1575)
- Fix regexp for compiler flags that contain spaces. [#1414](https://github.com/microsoft/vscode-cmake-tools/issues/1414)
- Fix compile active file when definition has quoted text. [#969](https://github.com/microsoft/vscode-cmake-tools/issues/969)
- Re-register the tasks provider when the current build targe changes. [#1576](https://github.com/microsoft/vscode-cmake-tools/issues/1576)
- Don't localize the VS Clang kit name. [PR [#1632](https://github.com/microsoft/vscode-cmake-tools/issues/1632)](https://github.com/microsoft/vscode-cmake-tools/pull/1632)
- Remove CMake Tools activation of non CMake projects when tasks.runask is executed. [PR [#1642](https://github.com/microsoft/vscode-cmake-tools/issues/1642)](https://github.com/microsoft/vscode-cmake-tools/pull/1642)
- Add the TWXS CMake extension in the CMake Tools extension pack. [PR [#1643](https://github.com/microsoft/vscode-cmake-tools/issues/1643)](https://github.com/microsoft/vscode-cmake-tools/pull/1643)

## 1.5.3
Bug Fixes:
- "Clean all projects" broken since 1.5.0. [#1542](https://github.com/microsoft/vscode-cmake-tools/issues/1542)
- CMake task provider should not attempt to register until the CMake driver is available.  [#1549](https://github.com/microsoft/vscode-cmake-tools/issues/1549)

## 1.5.2
Bug Fixes:
- Fix deadlock caused by commands invoked in string expansion during activation. [PR [#1532](https://github.com/microsoft/vscode-cmake-tools/issues/1532)](https://github.com/microsoft/vscode-cmake-tools/pull/1532)

## 1.5.1
Bug Fixes:
- Fix regular expression for variables values used in settings and kits json. [#1526](https://github.com/microsoft/vscode-cmake-tools/issues/1526) [#1525](https://github.com/microsoft/vscode-cmake-tools/issues/1525)
- Add a setting to control whether the Touch Bar is visible or not. [PR [#1529](https://github.com/microsoft/vscode-cmake-tools/issues/1529)](https://github.com/microsoft/vscode-cmake-tools/pull/1529)

## 1.5.0
Improvements:
- Support variables for Kit.toolchainFile. [PR [#991](https://github.com/microsoft/vscode-cmake-tools/issues/991)](https://github.com/microsoft/vscode-cmake-tools/pull/991) [#1056](https://github.com/microsoft/vscode-cmake-tools/issues/1056) [@blakehurd](https://github.com/blakehurd)/[@bobbrow](https://github.com/bobbrow)
- Implement cmake:hideBuildCommand context option. [PR [#1355](https://github.com/microsoft/vscode-cmake-tools/issues/1355)](https://github.com/microsoft/vscode-cmake-tools/pull/1355) [@tritao](https://github.com/tritao)
- Add option to set CMAKE_BUILD_TYPE also on multi-config generators. [PR [#1393](https://github.com/microsoft/vscode-cmake-tools/issues/1393)](https://github.com/microsoft/vscode-cmake-tools/pull/1393) [@tonka3000](https://github.com/tonka3000)
- Detect Clang for MSVC (GNU CLI) kits. [#823](https://github.com/microsoft/vscode-cmake-tools/issues/823) [@omcnoe](https://github.com/omcnoe)
- GUI support for CMake Tools cache. [#513](https://github.com/microsoft/vscode-cmake-tools/issues/513) [@nieroger](https://github.com/nieroger)
- Tasks support. [PR [#1268](https://github.com/microsoft/vscode-cmake-tools/issues/1268)](https://github.com/microsoft/vscode-cmake-tools/pull/1268) [@vptrbv](https://github.com/vptrbv)
- MacBook Pro touchbar support. [#499](https://github.com/microsoft/vscode-cmake-tools/issues/499) [@vptrbv](https://github.com/vptrbv)

Bug Fixes:
- Set right base_path for variant config files. [PR [#1462](https://github.com/microsoft/vscode-cmake-tools/issues/1462)](https://github.com/microsoft/vscode-cmake-tools/pull/1462) [@leolcao](https://github.com/leolcao)
- Inconsistent buildType substitution. [#1366](https://github.com/microsoft/vscode-cmake-tools/issues/1366)
- ${workspaceFolder} is not working for "environmentSetupScript" option. [#1309](https://github.com/microsoft/vscode-cmake-tools/issues/1309) [@Yaxley123](https://github.com/Yaxley123)
- Preserve focus when executing "CMake:Run Without Debugging". [#1138](https://github.com/microsoft/vscode-cmake-tools/issues/1138) [@estshorter](https://github.com/estshorter)
- Problems with CMake: Quick Start. [#1004](https://github.com/microsoft/vscode-cmake-tools/issues/1004) [@alan-wr](https://github.com/alan-wr)
- Remove depends on optimist by upgrade handlebars. [PR [#1447](https://github.com/microsoft/vscode-cmake-tools/issues/1447)](https://github.com/microsoft/vscode-cmake-tools/pull/1447) [@lygstate](https://github.com/lygstate)
- Ignore the vcvars dev-bat call result. [PR [#1403](https://github.com/microsoft/vscode-cmake-tools/issues/1403)](https://github.com/microsoft/vscode-cmake-tools/pull/1403) [@lygstate](https://github.com/lygstate)
- Fix vs2010 which doesn't recognize host=x64. [PR [#1481](https://github.com/microsoft/vscode-cmake-tools/issues/1481)](https://github.com/microsoft/vscode-cmake-tools/pull/1481) [@lygstate](https://github.com/lygstate)
- Don't rebuild when doing command substitution. [#1487](https://github.com/microsoft/vscode-cmake-tools/issues/1487)
- Duplicate compiler flags should not be removed. [PR [#1497](https://github.com/microsoft/vscode-cmake-tools/issues/1497)](https://github.com/microsoft/vscode-cmake-tools/issues/1497)
- Hide "Unknown Language" for CUDA source files. [PR [#1502](https://github.com/microsoft/vscode-cmake-tools/issues/1502)](https://github.com/microsoft/vscode-cmake-tools/issues/1502) [@Synxis](https://github.com/Synxis)
- Ensure immediate effect of settings for communication mode and all generator related. [PR [#1500](https://github.com/microsoft/vscode-cmake-tools/issues/1500)](https://github.com/microsoft/vscode-cmake-tools/issues/1500)
- Fix shell script and vcvars devbat when TEMP folder has a space in the middle. [#1492](https://github.com/microsoft/vscode-cmake-tools/issues/1492)

## 1.4.2
Improvements:
- Added new variable substitution command: `${command:cmake.launchTargetFilename}`. [#632](https://github.com/microsoft/vscode-cmake-tools/issues/632) [@ebai101](https://github.com/ebai101)
- Add output parser for Wind River Diab compiler. [PR [#1267](https://github.com/microsoft/vscode-cmake-tools/issues/1267)](https://github.com/microsoft/vscode-cmake-tools/pull/1267) [@ce3a](https://github.com/ce3a)
- Set application run directory to executable path. [#1395](https://github.com/microsoft/vscode-cmake-tools/issues/1395) [@Shatur95](https://github.com/Shatur95)

Bug Fixes:
- Allow minor version of File API protocol to be greater than expected. [#1341](https://github.com/microsoft/vscode-cmake-tools/issues/1341) [@KyleFromKitware](https://github.com/KyleFromKitware)
- Fix high-hitting crash related to output stream encoding. [PR [#1367](https://github.com/microsoft/vscode-cmake-tools/issues/1367)](https://github.com/microsoft/vscode-cmake-tools/issues/1367)
- Fix high-hitting crash: "message must be set" introduced by VS Code 1.49.0. [#1432](https://github.com/microsoft/vscode-cmake-tools/issues/1432)
- Fix detection of clang 10 on Debian. [#1330](https://github.com/microsoft/vscode-cmake-tools/issues/1330)
- Detect gdb for msys2 MinGW properly. [PR [#1338](https://github.com/microsoft/vscode-cmake-tools/issues/1338)](https://github.com/microsoft/vscode-cmake-tools/issues/1338) [@lygstate](https://github.com/lygstate)

## 1.4.1
Bug Fixes:
- VS environment not set correctly. [#1243](https://github.com/microsoft/vscode-cmake-tools/issues/1243)
- VS kits don't set host/target arch properly for toolsets. [#1256](https://github.com/microsoft/vscode-cmake-tools/issues/1256)
- Disable launchTarget key binding while debugging. [#1170](https://github.com/microsoft/vscode-cmake-tools/issues/1170)
- System headers not found. [#1257](https://github.com/microsoft/vscode-cmake-tools/issues/1257)
- Add setting to enable/disable automatic reconfiguring of projects. [#1259](https://github.com/microsoft/vscode-cmake-tools/issues/1259)
- Partial/full CMT activation improperly persisted for multi-root projects. [#1269](https://github.com/microsoft/vscode-cmake-tools/issues/1269)
- Fix MacOS debugging to work out of the box. [#1284](https://github.com/microsoft/vscode-cmake-tools/issues/1284)
- Ensure the silent kits scanning is run once for multi-root. [#1302](https://github.com/microsoft/vscode-cmake-tools/issues/1302)

## 1.4.0
Improvements:
- Documentation updates. [PR [#1130](https://github.com/microsoft/vscode-cmake-tools/issues/1130)](https://github.com/microsoft/vscode-cmake-tools/pull/1130) [@zalava](https://github.com/zalava)
- Add support for per-folder browse path. [#1073](https://github.com/microsoft/vscode-cmake-tools/issues/1073)
- Use a shell script to set environment variables for a kit. [#809](https://github.com/microsoft/vscode-cmake-tools/issues/809) [@pisker](https://github.com/pisker)
- Improvements of the status bar UI. [PR [#1200](https://github.com/microsoft/vscode-cmake-tools/issues/1200)](https://github.com/microsoft/vscode-cmake-tools/pull/1200) [@SchweizS](https://github.com/SchweizS)
- Add context menu for CMakeLists. [#741](https://github.com/microsoft/vscode-cmake-tools/issues/741) [@SchweizS](https://github.com/SchweizS)
- Support partial CMake Tools activation for non cmake repos. [#1167](https://github.com/microsoft/vscode-cmake-tools/issues/1167)
- Support ARM IntelliSense modes. [#1155](https://github.com/microsoft/vscode-cmake-tools/issues/1155)
- Support GNU language standards. [#1208](https://github.com/microsoft/vscode-cmake-tools/issues/1208)
- Add indication of active workspace to project outline. [#1183](https://github.com/microsoft/vscode-cmake-tools/issues/1183) [@SchweizS](https://github.com/SchweizS)

Bug Fixes:
- Skip over debugger guessing logic if cmake.debugConfig explicitly sets miDebuggerPath. [#1060](https://github.com/microsoft/vscode-cmake-tools/issues/1060)
- Normalize all paths sent to CppTools. [#1099](https://github.com/microsoft/vscode-cmake-tools/issues/1099)
- Add support for Objective-C and Objective-C++. [#1108](https://github.com/microsoft/vscode-cmake-tools/issues/1108) [@marksisson](https://github.com/marksisson)
- Update the configuration provider id. [#1045](https://github.com/microsoft/vscode-cmake-tools/issues/1045) [@ChristianS99](https://github.com/ChristianS99)
- Clear the terminal for Compile Active File. [#1122](https://github.com/microsoft/vscode-cmake-tools/issues/1122)
- Update vswhere to a version that supports utf-8. [#1104](https://github.com/microsoft/vscode-cmake-tools/issues/1104)
- Support source files outside the base path. [#1140](https://github.com/microsoft/vscode-cmake-tools/issues/1140)
- Allow quotes in cache entries. [#1124](https://github.com/microsoft/vscode-cmake-tools/issues/1124) [@tmaslach](https://github.com/tmaslach)
- Fix default preferred generators detection logic. [#1084](https://github.com/microsoft/vscode-cmake-tools/issues/1084)
- Fix host and target platform information for VS kits. [#964](https://github.com/microsoft/vscode-cmake-tools/issues/964)
- Fix error caused by duplicate project structure. [#587](https://github.com/microsoft/vscode-cmake-tools/issues/587) [@SchweizS](https://github.com/SchweizS)
- Disable launchTarget key binding while debugging. [#1170](https://github.com/microsoft/vscode-cmake-tools/issues/1170)
- Skip configuring when cache is present and according setting is on. [#984](https://github.com/microsoft/vscode-cmake-tools/issues/984)
- Remove deprecated cmake.useCMakeServer setting. [#1059](https://github.com/microsoft/vscode-cmake-tools/issues/1059)
- Trigger automatic CMake configure on CMakeLists.txt save. [#1187](https://github.com/microsoft/vscode-cmake-tools/issues/1187) [@Yuri6037](https://github.com/Yuri6037)
- Silently scanning for kits:
    - when there is no available kits json file. [PR [#1192](https://github.com/microsoft/vscode-cmake-tools/issues/1192)](https://github.com/microsoft/vscode-cmake-tools/pull/1192)
    - when the extension introduces breaking changes in the kits definition. [#1195](https://github.com/microsoft/vscode-cmake-tools/issues/1195)
- Various unhandled exceptions and crash fixes:
    - "cannot read property 'length' of undefined" when CMake not found in path. [#1110](https://github.com/microsoft/vscode-cmake-tools/issues/1110)
    - "cannot read property 'uri' of undefined" called by cmake.buildDirectory command. [#1150](https://github.com/microsoft/vscode-cmake-tools/issues/1150)
    - high hitting crash in telemetry. [PR [#1154](https://github.com/microsoft/vscode-cmake-tools/issues/1154)](https://github.com/microsoft/vscode-cmake-tools/pull/1154)

## 1.3.1
Improvements:
- Show "Collapse all" command on project outline view. [#839](https://github.com/microsoft/vscode-cmake-tools/issues/839) [@dirondin](https://github.com/dirondin)

Bug Fixes:
- Toolset and platform are swapped when reading from CMake cache. [#1065](https://github.com/microsoft/vscode-cmake-tools/issues/1065)
- Unable to debug targets when path is specified as absolute by the cmake-file-api. [#1067](https://github.com/microsoft/vscode-cmake-tools/issues/1067) [@KoeMai](https://github.com/KoeMai)

## 1.3.0
Improvements:
- Multi-root support. You can now open multiple folders in VS Code and CMake Tools will allow you to configure each of the projects in those folders.
- Add support for `${command:cmake.buildKit}`. [#334](https://github.com/microsoft/vscode-cmake-tools/issues/334) [@xgdgsc](https://github.com/xgdgsc)
- Add LLVM_ROOT and Visual Studio Clang locations to the search path for Kits. [#914](https://github.com/microsoft/vscode-cmake-tools/issues/914) [@Zingam](https://github.com/Zingam)
- Support additional `intelliSenseModes` in the configuration provider. [#960](https://github.com/microsoft/vscode-cmake-tools/issues/960)
- Detect bundled CMake in Visual Studio. [#610](https://github.com/microsoft/vscode-cmake-tools/issues/610) [@Zingam](https://github.com/Zingam)
- Add "Scan for kits" option in kits QuickPick. [#864](https://github.com/microsoft/vscode-cmake-tools/issues/864) [@Zingam](https://github.com/Zingam)
- Implement the CMake File API. [PR [#720](https://github.com/microsoft/vscode-cmake-tools/issues/720)](https://github.com/microsoft/vscode-cmake-tools/pull/720) [@KoeMai](https://github.com/KoeMai)

Bug Fixes:
- Support temp folders not located on system drive. [PR [#974](https://github.com/microsoft/vscode-cmake-tools/issues/974)](https://github.com/microsoft/vscode-cmake-tools/pull/974) [@Carsten87](https://github.com/Carsten87)
- Add MinGW path to the environment. [PR [#983](https://github.com/microsoft/vscode-cmake-tools/issues/983)](https://github.com/microsoft/vscode-cmake-tools/pull/983)
- Don't do a clean build for utility targets. [#643](https://github.com/microsoft/vscode-cmake-tools/issues/643) [@rcxdude](https://github.com/rcxdude)
- Visual Studio builds should support `cmake.parallelJobs` setting. [PR [#975](https://github.com/microsoft/vscode-cmake-tools/issues/975)](https://github.com/microsoft/vscode-cmake-tools/pull/975) [@tonka3000](https://github.com/tonka3000)
- Fix build cancellation. [#946](https://github.com/microsoft/vscode-cmake-tools/issues/946) [#781](https://github.com/microsoft/vscode-cmake-tools/issues/781) [#522](https://github.com/microsoft/vscode-cmake-tools/issues/522) [@KoeMai](https://github.com/KoeMai)
- Normalize both absolute and relative paths. [PR [#963](https://github.com/microsoft/vscode-cmake-tools/issues/963)](https://github.com/microsoft/vscode-cmake-tools/pull/963) [@GeorchW](https://github.com/GeorchW)
- Filter out duplicate targets from the target selector. [#863](https://github.com/microsoft/vscode-cmake-tools/issues/863)
- Fix a crash when `chcp` is not found on the machine. [#977](https://github.com/microsoft/vscode-cmake-tools/issues/977)
- Don't fail if CMakeLists.txt was appended to sourceDirectory. [#1014](https://github.com/microsoft/vscode-cmake-tools/issues/1014)
- Mark all tests as 'not run' in case of build failure when running CTest. [PR [#980](https://github.com/microsoft/vscode-cmake-tools/issues/980)](https://github.com/microsoft/vscode-cmake-tools/pull/980) [@Morozov-5F](https://github.com/Morozov-5F)
- Add command to hide launch/debug commands and debug button. [PR [#1035](https://github.com/microsoft/vscode-cmake-tools/issues/1035)](https://github.com/microsoft/vscode-cmake-tools/pull/1035)
- Add support for `${workspaceFolderBasename}`. [#869](https://github.com/microsoft/vscode-cmake-tools/issues/869)
- Fix exception thrown by debug/launch commands. [#1036](https://github.com/microsoft/vscode-cmake-tools/issues/1036)

## 1.2.3
Bug fixes:
- CTest status bar button text appears malformed. [#911](https://github.com/microsoft/vscode-cmake-tools/issues/911)
- Cleanup fix for message "Platform undefined / toolset {}". [#913](https://github.com/microsoft/vscode-cmake-tools/issues/913)
- Fix incorrect file associations when language is unset. [#926](https://github.com/microsoft/vscode-cmake-tools/issues/926)

## 1.2.2
Bug fixes:
- Fix broken SchemaProvider. [#874](https://github.com/microsoft/vscode-cmake-tools/issues/874)
- Fix the RegExp for finding a debugger. [#884](https://github.com/microsoft/vscode-cmake-tools/issues/884)
- Update flow for missing CMakeLists.txt. [#533](https://github.com/microsoft/vscode-cmake-tools/issues/533)
- getVSInstallForKit should be a no-op on systems other than windows. [#886](https://github.com/microsoft/vscode-cmake-tools/issues/886)
- Include missing source directories in the custom browse path. [#882](https://github.com/microsoft/vscode-cmake-tools/issues/882)
- Handle exceptions thrown by spawn. [#895](https://github.com/microsoft/vscode-cmake-tools/issues/895)
- Various generators fixes:
    - [#900](https://github.com/microsoft/vscode-cmake-tools/issues/900)
    - [#880](https://github.com/microsoft/vscode-cmake-tools/issues/880)
    - [#885](https://github.com/microsoft/vscode-cmake-tools/issues/885)

## 1.2.1
Thank you to the following CMake Tools contributors: koemai, bjosa, emanspeaks, som1lse,
dcourtois, tsing80, andy-held, notskm, thezogoth, yokuyuki, dbird137, fabianogk, randshot.

**vector-of-bool** has moved on to other things and Microsoft is now maintaining this extension. Thank you **vector-of-bool**
for all of your hard work getting this extension to where it is today!

Breaking changes:
- The publisher id changes to ms-vscode.cmake-tools. This requires that you uninstall earlier versions of the extension.
- Scanning for kits is able to detect more accurately multiple VS installations.
  To achieve this, a Visual Studio kit is defined differently now in cmake-tools-kits.json:
  the "visualStudio" field represents an ID unique to the installation
  as opposed to "VisualStudio.${VS Version}" (which may be the same for multiple same year VS installations).
  The CMake Tools Extension is still able to work with the old definition VS kits,
  but for simplicity and to avoid duplicates in the json file it will prompt for permission to delete them
  each time a "Scan for kits" is performed.

Features:
- Support for localized messages.
- Cross compile support for CppTools integration.
- Adapt CppTools integration to API version 3. [#637](https://github.com/Microsoft/vscode-cmake-tools/issues/637)
- Expand kit environment variables. [#460](https://github.com/Microsoft/vscode-cmake-tools/issues/460)
- Add new commands: launchTargetDirectory, buildType, buildDirectory. [#334](https://github.com/Microsoft/vscode-cmake-tools/issues/334), [#654](https://github.com/Microsoft/vscode-cmake-tools/issues/654), [#564](https://github.com/Microsoft/vscode-cmake-tools/issues/564), [#559](https://github.com/Microsoft/vscode-cmake-tools/issues/559), [#695](https://github.com/Microsoft/vscode-cmake-tools/issues/695)
- Add support for VS2010.

Improvements:
- Restructuring of the CMake Driver.
- Improve stability of CMake Generator Selection. [#512](https://github.com/Microsoft/vscode-cmake-tools/issues/512)
- Refactor and extend CMS-server driver test.
- Rework the CMake Build from a terminal to a task.
- Add Launch target test.
- Increase wait time in test to open terminal.

Bug fixes:
- Cannot execute current target without a debugger. [#601](https://github.com/Microsoft/vscode-cmake-tools/issues/601)
- Path clobbering by bad kit file env. [#701](https://github.com/Microsoft/vscode-cmake-tools/issues/701), [#713](https://github.com/Microsoft/vscode-cmake-tools/issues/713)
- Target install missing. [#504](https://github.com/Microsoft/vscode-cmake-tools/issues/504)
- CTest controller updated on reconfig. [#212](https://github.com/Microsoft/vscode-cmake-tools/issues/212)
- Recalculate total for every run of CTest.
- Debug target does not find GDB. [#375](https://github.com/Microsoft/vscode-cmake-tools/issues/375)

## 1.1.3

Many thanks to [Yonggang Luo](https://github.com/lygstate) for several changes
in this version.

Removal:

- The visual CMake cache editor GUI is gone. The API with which it was drawn is
  being removed from a future version of VS Code, and the feature had many
  issues. A future CMake GUI will be introduced with more features and greater
  stability.

Features and Tweaks:

- On Linux, will detect old CMake versions and offer to do an automatic
  upgrade. Windows support is pending. If you have a macOS devices and would
  like to contribute, please open a pull request!
- Smarter parsing of GCC and Clang compile errors to fold `note:` and
  `required from:` blocks into their main diagnostic. This permits the
  folding and browsing of template and macro instantiation errors in a nicer
  fashion. MSVC error parsing pending. (**NOTE**: There is an upstream issue
  with the sort order of diagnostic information, so `required from`
  tracebacks may appear out-of-order).

Fixes:

- On Windows, "Launch target in terminal" will use `cmd.exe` unconditionally.
  This works around issues with command quoting in PowerShell
- "Debug target" will prefer `lldb-mi` to `lldb`. Fixes issues where `cpptools`
  is unable to launch the debugger.
- Document the `environmentVariables` field on kits.
- Fix legacy CMake mode not setting the CMake generator.
- Permit limited variable expansion for `cmake.cmakePath` in `settings.json`
  (refer to documentation for more details).

## 1.1.2

A bugfix release for [these issues](https://github.com/vector-of-bool/vscode-cmake-tools/milestone/13?closed=1).

## 1.1.1

A bugfix release for [these issues](https://github.com/vector-of-bool/vscode-cmake-tools/milestone/12?closed=1).

**BREAKING CHANGE**: Variant substitutions follow a new `${variant:var-key}`
syntax to match the special namespacing of substitutions.

## 1.1.0

1.1.0 includes a few new major features:

- `cpptools` integration for IntelliSense
- A Project Outline view as a custom explorer
- Building individual source files from the editor menus
- New UI for progress and cancellation

See the changelog in the official documentation for more information.
