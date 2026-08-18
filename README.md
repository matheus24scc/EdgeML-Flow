# EdgeML‑Flow  
**Drag‑and‑drop studio for designing, training, and deploying TensorFlow Lite Micro and PyTorch Mobile models to microcontrollers with OTA updates.**

---

## Overview  
EdgeML‑Flow unifies the entire edge‑AI workflow into a single drag‑and‑drop studio. From data collection on the device, through edge‑optimized training (quantization‑aware neural architecture search), to secure over‑the‑air flashing via Manifest‑based update pipelines, developers can turn battery‑operated microcontrollers into intelligent sensors for predictive maintenance, gesture control, environmental monitoring, and more—without leaving the browser‑based studio.

## Core Innovation  
A **unified workflow** that stitches together best‑of‑breed edge‑ML tooling (TensorFlow Lite Micro, Edge Impulse, PyTorch Lightning) with proven OTA standards (Manifest‑based updates, MQTT/SN, Web‑Bluetooth). By exposing the entire pipeline as a WebAssembly‑powered UI, EdgeML‑Flow lets contributors plug in new model optimizers, UI widgets, or device‑specific drivers while delivering a tangible end‑to‑end edge AI pipeline that runs on FreeRTOS, Zephyr, and similar RTOSes.

## Tech Stack  

| Layer | Technology |
|-------|------------|
| **UI / Studio** | WebAssembly (Blazor/React), TypeScript, CSS3 |
| **Modeling & Training** | Python (TensorFlow Lite, PyTorch Lightning), Edge Impulse CLI |
| **Model Optimization** | Quantization‑aware Neural Architecture Search (Q‑NAS) |
| **Device SDK** | C/C++ SDK, FreeRTOS, Zephyr RTOS |
| **Communication** | MQTT‑SN, Web‑Bluetooth, HTTPS (for OTA manifests) |
| **OTA Update** | Manifest‑based update protocol (SWUDM‑like) |
| **Build & CI** | GitHub Actions, Docker, CMake, PlatformIO |
| **Testing** | PyTest, GoogleTest, Hardware‑in‑the‑Loop (HIL) scripts |

## Getting Started  

### Prerequisites  
- **Python ≥3.9** (with `pip` and `virtualenv`)  
- **Node.js ≥18** (for the WebAssembly UI)  
- **CMake ≥3.20** and a C/C++ toolchain (GCC ARM Embedded or Zephyr SDK)  
- **Docker** (optional, for containerized builds)  
- A supported MCU board (e.g., Nordic nRF52840, STM32L4, ESP32‑C3) with JTAG/SWD or USB‑DFU capability  

### Installation  

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-org/EdgeML-Flow.git
cd EdgeML-Flow

# 2️⃣ Set up the Python environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3️⃣ Install the WebAssembly UI dependencies
npm install
npm run build-wasm   # builds the WASM UI bundle

# 4️⃣ Install device‑side SDK (example for Zephyr)
west init -m https://github.com/zephyrproject-rtos/zephyr
west update
zephyr-sdk-0.16.0/setup.sh   # adjust version as needed

# 5️⃣ (Optional) Pull Edge Impulse CLI for data labeling
npm install -g edge-impulse-cli
```

### Usage  

1. **Launch the Studio**  
   ```bash
   npm run start   # serves the WASM UI at http://localhost:3000
   ```

2. **Collect Data**  
   - Connect your MCU via USB‑DFU or JTAG.  
   - Use the *Data Capture* widget to stream sensor streams (accelerometer, microphone, etc.) and label samples directly in the UI.

3. **Design & Train**  
   - Drag‑drop preprocessing blocks (filter, normalize, window).  
   - Choose a model backbone (CNN, RNN, TinyML‑NAS).  
   - Enable *Quantization‑Aware NAS* to search for latency‑accurate configurations.  
   - Hit **Train** – the backend runs a PyTorch Lightning job (optionally on GPU) and exports a `.tflite` or `.pt` file.

4. **Optimize & Export**  
   - The studio runs post‑training quantization and optionally generates a C‑compatible model library (`model_data.cc`, `model_data.h`).  

5. **OTA Deploy**  
   - Plug your device into the workstation; the studio flashes the bootloader and the initial firmware.  
   - Subsequent updates are delivered over MQTT‑SN or Web‑Bluetooth using a Manifest file that describes the new model binary, version, and cryptographic signature.  

6. **Monitor & Iterate**  
   - The device streams inference metrics (latency, power, accuracy) back to the studio for live monitoring.  
   - Tweak the pipeline and redeploy OTA without opening the enclosure.

### Quick Demo  
```bash
# Run the end‑to‑end demo on an nRF52840 DK
./scripts/demo_nrf52840.sh   # flashes a gesture‑recognition model and streams predictions
```

## Roadmap  

| Quarter | Milestone |
|---------|-----------|
| **Q3 2025** | *Alpha release*: Core studio UI, data capture, basic TFLite Micro export, manual JTAG flash. |
| **Q4 2025** | *Beta 1*: Quantization‑Aware NAS integration, OTA Manifest support over MQTT‑SN, first‑party Zephyr & FreeRTOS ports. |
| **Q1 2026** | *Beta 2*: Web‑Bluetooth OTA, model‑size profiler, power‑estimation widget, community plugin system. |
| **Q2 2026** | *GA release*: Stable SDK, CI/CD pipeline for automated model‑to‑firmware pipelines, documentation & tutorials. |
| **H2 2026** | *Ecosystem*: Marketplace for community‑contributed model blocks, device drivers, and UI widgets. |

## Contributing  

We welcome contributions from the community! Whether you’re fixing bugs, adding new model optimizers, creating UI widgets, or porting to a new MCU, your help makes EdgeML‑Flow better.

1. **Fork** the repository.  
2. Create a **feature branch** off `main`: `git checkout -b feature/awesome-feature`.  
3. Make your changes, ensuring you follow the existing code style (see `CODE_STYLE.md`).  
4. Add or update tests as needed (`pytest` for Python, `unity` for C).  
5. Run the full test suite locally:  
   ```bash
   pytest && ./scripts/run_c_tests.sh
   ```  
6. Commit with a clear message and push to your fork.  
7. Open a **Pull Request** against `main`.  
   - Include a description of the problem and solution.  
   - Link to any related issues.  
   - Ensure all CI checks pass.

Please read our **[CONTRIBUTING.md](CONTRIBUTING.md)** for detailed guidelines, licensing, and code of conduct.

## License  

EdgeML‑Flow is released under the **Apache License 2.0** – see the [LICENSE](LICENSE) file for details.

## Acknowledgments  

- **TensorFlow Lite Micro** – for the ultra‑low‑latency inference engine.  
- **Edge Impulse** – for inspiration on data collection and labeling workflows.  
- **PyTorch Lightning** – for simplifying scalable model training.  
- **Zephyr Project** & **FreeRTOS** – for providing robust, production‑grade RTOS foundations.  
- **WebAssembly community** – for enabling high‑performance UI in the browser.  
- **Open Source Contributors** – whose libraries and tools make edge AI accessible to all.  

*Built with ❤️ by the EdgeML‑Flow team.*  

---  

*Ready to push intelligence to the edge? Star the repo, grab a board, and start dragging.*

## Status (checkup 2026-08-18)
> Revisado na campanha de repo-checkup. Relatorio completo: `~/repo-checkup/reports/EdgeML-Flow.md` (local do mantenedor, nao no repo).
- **Build/Install**: scaffold/referencia sem build
- **Smoke test**: N/A
- **Para rodar de ponta-a-ponta precisa de**: nenhum servico externo
- **Inconsistencias conhecidas (README vs codigo)**: nenhuma
- **Seguranca**: sem vulns altas remediadas automaticamente
- **Estado resumido**: scaffold/referencia sem app para rodar
