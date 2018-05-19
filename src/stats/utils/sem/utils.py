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


def print_campaign_information(campaign):
    """
    Print information about the current campaign.
    """
    pprint.PrettyPrinter(indent=4).print(
        campaign.db.get_campaign_information())


def get_current_commit(path):
    """
    Return a string containing the hash of the current commit.
    """


def get_parameter_combinations(parameter_space):
    """
    Return a list of all parameter combinations that lie in the specified
    parameter space.
    """


def get_available_parameters(campaign):
    """
    Get a list of the parameters available in the campaign.
    """
