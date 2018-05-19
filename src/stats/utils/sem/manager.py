# /*
#  * This program is free software; you can redistribute it and/or modify
#  * it under the terms of the GNU General Public License version 2 as
#  * published by the Free Software Foundation;
#  *
#  * This program is distributed in the hope that it will be useful,
#  * but WITHOUT ANY WARRANTY; without even the implied warranty of
#  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  * GNU General Public License for more details.
#  *
#  * You should have received a copy of the GNU General Public License
#  * along with this program; if not, write to the Free Software
#  * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#  *
#  */

import pprint
from .database import DatabaseManager
from .runner import SimulationRunner


class CampaignManager(object):
    """
    The main Simulation Execution Manager class, which can be used to load,
    save, execute and access the results of simulation campaigns.
    """

    #######################################
    # Campaign initialization and loading #
    #######################################

    def __init__(self, campaign_db):
        """
        Initialize the Simulation Execution Manager.
        """
        self.db = campaign_db
        self.runner = SimulationRunner(self.db)

    @classmethod
    def new_from_config(cls, campaign_config, filename):
        """
        Read a dictionary describing the campaign configuration and initialize
        a corresponding campaign database.
        """
        # return cls(campaign_db)

    @classmethod
    def load_from_file(cls, filename):
        """
        Read a filename and load the corresponding campaign database.
        """
        # Create DatabaseManager from file
        # return cls(campaign_db)

    ######################
    # Simulation running #
    ######################

    def run_simulations(self, parameter_space):
        """
        Run the missing simulations from a dictionary containing parameter -
        array of values pairs, defining the parameter space to explore.
        """
        # Offload simulation execution to self.runner

    #####################
    # Result management #
    #####################

    def get_results_as_numpy_array(self, parameter_space):
        """
        Return the results relative to the desired parameter space in the form
        of a numpy array.
        """
        # Collect list of relevant results from DatabaseManager
        # Package results in a numpy array
