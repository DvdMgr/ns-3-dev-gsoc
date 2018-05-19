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

from tinydb import TinyDB


class DatabaseManager(object):
    """
    The class tasked with interfacing to the simulation campaign database.
    """

    ##################
    # Initialization #
    ##################

    def __init__(self, db):
        """
        Initialize the DatabaseManager with a TinyDB instance.
        """
        self.db = db

    @classmethod
    def load_from_file(self, filename):
        """
        Initialize from an existing database.
        """
        # Read TinyDB instance from file
        # Check validity of database file
        # return db

    @classmethod
    def new_from_config(self, config, filename):
        """
        Initialize a new instance with a set filename.
        """
        # Create new TinyDB instance
        # Save db to file
        # return db

    ###################
    # Database access #
    ###################

    def get_config(self):
        """
        Return the configuration dictionary of this DatabaseManager's campaign
        """
        # Read from self.db and return the config entry of the database

    def get_results(self, parameters):
        """
        Return the currently available results which correspond to the
        specified parameter space.

        parameters: dictionary containing name-value(s) pairs for each one of
        the available parameters.
        """

    def insert_config(self, config):
        """
        Insert a configuration in the database.
        """

    def insert_result(self, result):
        """
        Insert a new result in the database.
        """
