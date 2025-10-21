# ✨ Pegasus DevContainer - Simple Setup

## What's New

A minimal DevContainer config that:
- Matches the GitHub Actions CI setup
- Works out of the box
- Takes ~5-10 minutes to set up on first run
- Uses only 4 files (instead of 8+)

## Files

```
.devcontainer/
├── devcontainer.json    ← VS Code config (one line per setting)
├── post-create.sh       ← Auto-runs setup script
├── Dockerfile           ← Not used (using pre-built image)
└── README.md           ← Quick help
```

## Get Started (3 Steps)

1. **Open in VS Code**
   ```bash
   code /path/to/pegasus
   ```

2. **Reopen in container**
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P`)
   - Type: `Dev Containers: Reopen in Container`
   - Wait ~5-10 minutes ⏳

3. **Start coding!**
   ```bash
   pytest tests/
   ```

## What Happens Automatically

✅ Ubuntu 24.04 + Python 3.12  
✅ System deps (FFTW3, Java)  
✅ All Pegasus packages (with R for rpy2)  
✅ Test tools (pytest, coverage)  
✅ Test data cloned  
✅ Jupyter on port 8888  

## Common Tasks

```bash
# Run tests
pytest tests/
pytest tests/test_seurat_comprehensive.py -v

# Start Jupyter
jupyter lab --ip=0.0.0.0

# View CLI
python -m pegasus --help

# Reinstall package
pip install -e ".[all]"
```

## Make Changes

**Add a package?**
```bash
pip install package-name
```

**Change Python version?**
Edit `devcontainer.json`:
```json
"image": "mcr.microsoft.com/devcontainers/python:3.11-ubuntu-24.04"
```

**Add system package?**
Edit `post-create.sh`:
```bash
sudo apt-get install -y your-package
```

**Rebuild container?**
- `Ctrl+Shift+P` → `Dev Containers: Rebuild Container`

## Troubleshoot

**Setup failing?**
```bash
bash .devcontainer/post-create.sh
```

**Test data missing?**
```bash
git clone https://github.com/lilab-bcb/pegasus-test-data.git ./tests/data
```

**Out of memory?**
- Open Docker Desktop → Settings → Resources
- Increase Memory to 8GB+

**Need help?**
See `.devcontainer/README.md`

## That's It! 🎉

No complex setup. Just:
1. Open container
2. Wait
3. Code
