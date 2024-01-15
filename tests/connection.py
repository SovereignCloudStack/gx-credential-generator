from openstack.image.v2.image import Image
from typing import List


class TestConnection:
    """
    Wrap connection to OpenStack Cluster
    """
    images = []

    def __init__(self, images: List[Image]):
        self.images = images

    def list_images(self):
        return self.images
