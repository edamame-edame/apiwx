# Makefile for apiwx project automation
# Cross-platform build automation

# Variables
PYTHON := python
PROJECT_NAME := apiwx
BUILD_SCRIPT := build.py
CONFIG_FILE := build.json
TEST_SCRIPT := test/run_tests.py

# Colors for output
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

# Default target
.PHONY: all
all: build

# Help target
.PHONY: help
help:
	@echo "$(GREEN)apiwx Build Automation$(NC)"
	@echo ""
	@echo "Available targets:"
	@echo "  $(YELLOW)build$(NC)         - Build packages with current version"
	@echo "  $(YELLOW)release$(NC)       - Build packages with version bump (use VERSION=x.y.z)"
	@echo "  $(YELLOW)test$(NC)          - Run test suite"
	@echo "  $(YELLOW)clean$(NC)         - Clean build artifacts"
	@echo "  $(YELLOW)install$(NC)       - Install package in development mode"
	@echo "  $(YELLOW)uninstall$(NC)     - Uninstall package"
	@echo "  $(YELLOW)validate$(NC)      - Validate environment and configuration"
	@echo "  $(YELLOW)lint$(NC)          - Run code linting (if available)"
	@echo "  $(YELLOW)format$(NC)        - Format code (if available)"
	@echo ""
	@echo "Examples:"
	@echo "  make build"
	@echo "  make release VERSION=0.1.15"
	@echo "  make test"

# Build with current version
.PHONY: build
build:
	@echo "$(GREEN)Building $(PROJECT_NAME)...$(NC)"
	$(PYTHON) $(BUILD_SCRIPT)

# Build with version update
.PHONY: release
release:
	@if [ -z "$(VERSION)" ]; then \
		echo "$(RED)Error: VERSION not specified. Use: make release VERSION=x.y.z$(NC)"; \
		exit 1; \
	fi
	@echo "$(GREEN)Building $(PROJECT_NAME) version $(VERSION)...$(NC)"
	$(PYTHON) $(BUILD_SCRIPT) --version $(VERSION)

# Run tests
.PHONY: test
test:
	@echo "$(GREEN)Running tests...$(NC)"
	$(PYTHON) $(TEST_SCRIPT)

# Clean build artifacts
.PHONY: clean
clean:
	@echo "$(GREEN)Cleaning build artifacts...$(NC)"
	$(PYTHON) setup.py clean --all
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Install in development mode
.PHONY: install
install:
	@echo "$(GREEN)Installing $(PROJECT_NAME) in development mode...$(NC)"
	$(PYTHON) -m pip install -e .

# Uninstall package
.PHONY: uninstall
uninstall:
	@echo "$(GREEN)Uninstalling $(PROJECT_NAME)...$(NC)"
	$(PYTHON) -m pip uninstall $(PROJECT_NAME) -y

# Validate environment
.PHONY: validate
validate:
	@echo "$(GREEN)Validating environment...$(NC)"
	@if [ ! -f "$(CONFIG_FILE)" ]; then \
		echo "$(RED)Error: Configuration file $(CONFIG_FILE) not found$(NC)"; \
		exit 1; \
	fi
	@if [ ! -f "setup.py" ]; then \
		echo "$(RED)Error: setup.py not found$(NC)"; \
		exit 1; \
	fi
	@if [ ! -f "$(TEST_SCRIPT)" ]; then \
		echo "$(RED)Error: Test script $(TEST_SCRIPT) not found$(NC)"; \
		exit 1; \
	fi
	@echo "$(GREEN)✅ Environment validation passed$(NC)"

# Lint code (optional - requires flake8 or similar)
.PHONY: lint
lint:
	@echo "$(GREEN)Running code linting...$(NC)"
	-$(PYTHON) -m flake8 $(PROJECT_NAME)/ --max-line-length=100
	-$(PYTHON) -m pylint $(PROJECT_NAME)/ || true

# Format code (optional - requires black or similar)  
.PHONY: format
format:
	@echo "$(GREEN)Formatting code...$(NC)"
	-$(PYTHON) -m black $(PROJECT_NAME)/ test/
	-$(PYTHON) -m isort $(PROJECT_NAME)/ test/

# Quick build without tests
.PHONY: quick
quick:
	@echo "$(GREEN)Quick build (no tests)...$(NC)"
	$(PYTHON) $(BUILD_SCRIPT) --no-tests

# Build with custom config
.PHONY: custom-build
custom-build:
	@if [ -z "$(CONFIG)" ]; then \
		echo "$(RED)Error: CONFIG not specified. Use: make custom-build CONFIG=path/to/config.json$(NC)"; \
		exit 1; \
	fi
	@echo "$(GREEN)Building with custom config: $(CONFIG)$(NC)"
	$(PYTHON) $(BUILD_SCRIPT) --config $(CONFIG)

# Show package info
.PHONY: info
info:
	@echo "$(GREEN)Package Information:$(NC)"
	@$(PYTHON) -c "import sys; sys.path.insert(0, '.'); import $(PROJECT_NAME); print(f'Version: {$(PROJECT_NAME).__version__}'); print(f'Location: {$(PROJECT_NAME).__file__}')" 2>/dev/null || echo "Package not importable"

# List build artifacts
.PHONY: list
list:
	@echo "$(GREEN)Build Artifacts:$(NC)"
	@if [ -d "dist" ]; then \
		ls -la dist/; \
	else \
		echo "No dist/ directory found"; \
	fi

# Complete workflow: clean -> test -> build
.PHONY: full
full: clean test build
	@echo "$(GREEN)✅ Complete build workflow finished$(NC)"