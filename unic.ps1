# Activate Python virtual environment
$venv_folder = Join-Path -Path $PSScriptRoot -ChildPath "unic_venv"
& "$venv_folder/Scripts/Activate.ps1"

$x = $args[0]
$current_path = get-location
$argument = Join-Path -Path $current_path -ChildPath $x


# Run the command
python $PSScriptRoot/unic.py -n $argument
