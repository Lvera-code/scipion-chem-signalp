# **************************************************************************
# *
# * Authors:     Enzo Sierra (enzogael57@gmail.com)
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************
"""
This package contains a protocol for signal peptide prediction of a
full-length protein/construct using a local SignalP-6.0 installation.
"""

import os

from pwchem import Plugin as pwchemPlugin

from .constants import DEFAULT_BINARY_NAME, NOINSTALL_WARNING, SIGNALP_DIC

_references = ['Teufel2022']


class Plugin(pwchemPlugin):
    """SignalP-6.0 is academic-use only software (DTU Health Tech): it is
    never installed automatically. See ``validateInstallation`` for what is
    checked and ``README.rst`` for the manual installation steps."""

    @classmethod
    def _defineVariables(cls):
        cls._defineVar(SIGNALP_DIC['python_bin'], '')
        cls._defineVar(SIGNALP_DIC['binary_name'], DEFAULT_BINARY_NAME)
        cls._defineVar(SIGNALP_DIC['model_dir'], '')

    @classmethod
    def defineBinaries(cls, env):
        """No-op: SignalP-6.0 is never installed automatically (academic
        license, not redistributable). See ``validateInstallation``."""
        pass

    @classmethod
    def validateInstallation(cls):
        """Check that this plugin's requirements are met. Returns a list of
        actionable error messages, empty if the installation is correct."""
        errors = []

        pythonBin = cls.getVar(SIGNALP_DIC['python_bin'])
        binaryPath = cls.getSignalPBinaryPath()
        if not pythonBin or not os.path.isfile(pythonBin):
            errors.append(f"SIGNALP_PYTHON_BIN is not set or does not exist: '{pythonBin}'.")
        elif not binaryPath or not os.path.isfile(binaryPath):
            errors.append(f"Could not find the local SignalP-6.0 binary at '{binaryPath}'.")

        modelDir = cls.getVar(SIGNALP_DIC['model_dir'])
        if not modelDir or not os.path.isdir(os.path.join(modelDir or '', 'sequential_models_signalp6')):
            errors.append(
                f"Could not find 'sequential_models_signalp6/' under SIGNALP_MODEL_DIR: '{modelDir}'."
            )

        if errors:
            errors.append(NOINSTALL_WARNING)
        return errors

    # ---------------------------------- Utils -----------------------------------

    @classmethod
    def getSignalPBinaryPath(cls):
        pythonBin = cls.getVar(SIGNALP_DIC['python_bin'])
        if not pythonBin:
            return None
        return os.path.join(os.path.dirname(pythonBin), cls.getVar(SIGNALP_DIC['binary_name']))
