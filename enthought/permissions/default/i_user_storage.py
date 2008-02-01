#------------------------------------------------------------------------------
# Copyright (c) 2008, Riverbank Computing Limited
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Riverbank Computing Limited
# Description: <Enthought permissions package component>
#------------------------------------------------------------------------------


# Enthought library imports.
from enthought.traits.api import Interface


class UserStorageError(Exception):
    """This is the exception raised by an IUserStorage object when an error
    occurs accessing the database.  Its string representation is displayed as
    an error message to the user."""


class IUserStorage(Interface):
    """This defines the interface expected by a UserManager instance to handle
    the low level storage of the user data."""

    ###########################################################################
    # 'IUserStorage' interface.
    ###########################################################################

    def add_user(self, name, description, password):
        """Add a new user with the given name, description and password."""

    def delete_user(self, name):
        """Delete the user with the given name (which will not be empty)."""

    def get_user(self, name):
        """Return a tuple of the name, description, blob and password of the
        user with the given name."""

    def get_users(self, name):
        """Return a list of tuples of the full name, description, blob and
        password of all users that match the given name.  How the name is
        interpreted (eg. as a regular expression) is determined by the storage.
        """

    def is_empty(self):
        """Return True if the user database is empty.  It will only ever be
        called once."""

    def update_blob(self, name, blob):
        """Update the blob for the user with the given name (which will not be
        empty)."""

    def update_password(self, name, password):
        """Update the password for the user with the given name (which will not
        be empty)."""

    def update_user(self, name, description, password):
        """Update the description and password for the user with the given name
        (which will not be empty)."""