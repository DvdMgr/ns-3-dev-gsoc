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

# This is a simple example of how to use the ns-3 SimulationExecutionManager

from sem import CampaignManager

# Campaign creation
###################

param_space = {
    'tcpVariant': ["TcpHybla", "TcpHighSpeed", "TcpHtcp", "TcpVegas",
                   "TcpScalable", "TcpVeno", "TcpBic", "TcpYeah",
                   "TcpIllinois", "TcpWestwood", "TcpWestwoodPlus",
                   "TcpLedbat"],
    'runs': 10
}

config = {
    'script': 'wifi-tcp',
    'ns-3-path': "/path/to/ns-3/",
}

campaign = CampaignManager.new_from_config(config, 'example-campaign.json')

campaign.run_simulations(param_space)

campaign.get_results_as_numpy_array(param_space)

campaign.print_campaign_information()
