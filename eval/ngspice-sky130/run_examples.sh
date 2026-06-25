#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/examples"

for netlist in *.cir; do
  log="${netlist%.cir}.log"
  echo "running ${netlist}"
  ngspice -b "$netlist" >"$log" 2>&1
done

echo "ngspice examples passed"

