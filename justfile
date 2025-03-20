default:
    @just --list

pre-commit:
    uvx pre-commit run --all-files
