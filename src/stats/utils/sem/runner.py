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

class SimulationRunner(object):
    """
    The class tasked with running simulations.
    """

    ##################
    # Initialization #
    ##################

    def __init__(self, db):
        """
        Initialization, using a DatabaseManager.
        """
        self.db = db

    ######################
    # Simulation running #
    ######################

    def run_single_simulation(self, parameters):
        """
        Run a simulation using a certain combination of parameters.
        """

    def run_missing_simulations(self, parameter_space):
        """
        Run the simulations belonging to the parameter_space that are still
        missing from the database.
        """
