let
  sources = import ./nix/sources.nix;
  pkgs = import sources.nixpkgs { };
in pkgs.mkShell { buildInputs = with pkgs; [ nodejs-16_x yarn ]; }
