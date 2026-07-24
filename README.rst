================================
SignalP-6.0 Scipion plugin
================================

Scipion framework plugin wrapping SignalP-6.0 (Teufel et al. 2022, DTU
Health Tech, academic license) for N-terminal signal peptide prediction.

The plugin implements a single protocol, ``ProtSignalPPrediction``, which
annotates (does **not** filter) every input ROI with
``_signalpPrediction``/``_signalpProbOther``/``_signalpProbSp``/
``_signalpCsPosition``. Purpose in the construct-level check (Fase 8):
confirm a final assembled multi-epitope construct does NOT have a
predicted signal peptide at its N-terminal (a synthetic fusion construct
should not have one; a positive prediction flags an accidental
signal-like motif worth reviewing).

SignalP-6.0 is **not** bundled with this plugin: it must be downloaded
separately (academic email required) and pointed to via ``scipion.conf``.

================================
Download SignalP-6.0
================================

SignalP-6.0 is **academic-use only** software (DTU Health Tech). Request
it from:
https://services.healthtech.dtu.dk/services/SignalP-6.0/

Build a dedicated venv (Python 3.10, ``torch>1.7,<2`` per the package's
own pin, ``numpy<2`` -- otherwise a bare install pulls numpy>=2 via
matplotlib, breaking the ABI against the torch build, same bug class as
ToxinPred2). Then, in ``scipion.conf``, set:

.. code-block::

      SIGNALP_PYTHON_BIN = <path to the venv's python>
      SIGNALP_MODEL_DIR = <path to the folder containing sequential_models_signalp6/>

===================
Install this plugin
===================

**Developer's version**

.. code-block::

            git clone https://github.com/Lvera-code/scipion-chem-signalp.git
            cd scipion-chem-signalp
            scipion3 installp -p . --devel
