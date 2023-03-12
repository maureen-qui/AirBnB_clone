#!/usr/bin/python3
""" A class BaseModel that defines all attributes and methods"""
import datetime
import models
import uuid


class BaseModel:
    """ the BaseModel class of the Project"""

    def __init__(self, *args, **kwargs):
        """Initialization method for each instance
        Args:
            args: unknown number of arguments
            kwargs: unkown number of key/value arguments
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            form = "%Y-%m-%dT%H:%M:%S.%f"
            self.id = kwargs["id"]
            self.created_at = datetime.datetime.strptime(kwargs["created_at"],
                                                         form)
            self.updated_at = datetime.datetime.strptime(kwargs["updated_at"],
                                                         form)
        else:
            models.storage.new(self)

    def save(self):
        """updates the current date and time"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionary method to update and return a dictionary
        Returns:
            A dict
        """
        our_dict = self.__dict__.copy()
        our_dict["__class__"] = self.__class__.__name__
        our_dict["created_at"] = self.created_at.isoformat()
        our_dict["updated_at"] = self.updated_at.isoformat()
        return our_dict

    def __str__(self):
        """String method that prints a set of strings anytime it
            called
        Returns:
            A string
        """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
