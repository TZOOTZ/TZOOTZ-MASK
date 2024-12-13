# TZOOTZ▲MASK for ComfyUI

Advanced mask handling and denoise control node for ComfyUI, part of the TZOOTZ RESEARCH toolkit.

![TZOOTZ RESEARCH](https://img.shields.io/badge/TZOOTZ-RESEARCH-blue)
![ComfyUI](https://img.shields.io/badge/ComfyUI-node-green)
![Version](https://img.shields.io/badge/version-1.0-orange)

## Overview

TZOOTZ▲MASK is a specialized ComfyUI node designed to provide advanced control over the denoising process through intelligent mask handling and alpha channel processing.

## Features

- 🖼️ Intelligent image loading with file browser
- 🎭 Automatic alpha channel extraction
- 🎨 Mask generation for non-alpha images
- 🔄 Feathering/smoothing controls
- 📊 Dynamic denoise value calculation

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-username/comfyui_tzootz_research.git
```

2. Restart ComfyUI

## Usage

The node will appear in the "TZOOTZ RESEARCH" category in your node browser.

### Inputs
- `image`: Image file selector (supports PNG, JPEG, etc.)
- `feather_amount`: Smoothing control (0.0 - 1.0)

### Outputs
- `image`: Processed RGB image tensor
- `mask`: Generated/extracted mask tensor
- `denoise_value`: Calculated denoise value

## Technical Details

### File Structure
```
comfyui_tzootz_research/
├── __init__.py
└── tzootz_loader.py
```

### Dependencies
- PIL (Pillow)
- numpy
- torch
- ComfyUI core libraries

### Node Configuration
```python
RETURN_TYPES = ("IMAGE", "MASK", "FLOAT")
RETURN_NAMES = ("image", "mask", "denoise_value")
FUNCTION = "load_and_process"
CATEGORY = "TZOOTZ RESEARCH"
```

## Workflow Integration

TZOOTZ▲MASK is designed to integrate seamlessly with:
- KSampler nodes (denoise control)
- Image processing nodes
- Mask manipulation nodes
- Other TZOOTZ RESEARCH tools

## Development Status

### Implemented
- ✅ Basic image loading
- ✅ Alpha extraction
- ✅ Feathering control
- ✅ ComfyUI integration

### Planned Features
- 🚧 Preview system
- 🚧 Extended mask options
- 🚧 Preset system
- 🚧 Enhanced error handling

## Contributing

Contributions are welcome! Please check our [Contributing Guidelines](CONTRIBUTING.md) before submitting PRs.

## License

[MIT License](LICENSE)

## Acknowledgments

- ComfyUI Team
- TZOOTZ RESEARCH Contributors

## Contact

- GitHub Issues: [Report a bug](https://github.com/your-username/comfyui_tzootz_research/issues)
- TZOOTZ RESEARCH: [Official Website](#)

---
Created with 🔬 by TZOOTZ RESEARCH
