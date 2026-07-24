# -*- coding: utf-8 -*-
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

DEFAULT_VERSION = '6.0'

# SignalP-6.0 is academic-use only software (DTU Health Tech), not
# redistributable: same class of constraint as BepiPred/NetMHCpan/
# NetMHCIIpan -- it is never installed automatically. The user downloads
# it manually (institutional email required) and points to it via
# scipion.conf.
SIGNALP_DIC = {
    'name': 'SignalP',
    'version': DEFAULT_VERSION,
    'python_bin': 'SIGNALP_PYTHON_BIN',
    'binary_name': 'SIGNALP_BINARY_NAME',
    'model_dir': 'SIGNALP_MODEL_DIR',
}

DEFAULT_BINARY_NAME = 'signalp6'
DEFAULT_ORGANISM = 'other'

READ_URL = 'https://github.com/Lvera-code/scipion-chem-signalp'
DOWNLOAD_URL = 'https://services.healthtech.dtu.dk/services/SignalP-6.0/'

NOINSTALL_WARNING = (
    'Installation could not be completed because the local SignalP-6.0 '
    'installation has not been found. Due to academic license restrictions, '
    f'DTU Health Tech does not allow redistributing this package: download it '
    f'manually from {DOWNLOAD_URL} (requires an academic account), build a '
    'dedicated venv (Python 3.10, torch>1.7,<2, numpy<2 -- see README.rst for '
    'why these pins matter) and set SIGNALP_PYTHON_BIN/SIGNALP_MODEL_DIR in '
    f'scipion.conf. Please check the scipion-chem-signalp README file for '
    f'more details: {READ_URL}'
)
