from typing import Callable, Optional
from warnings import warn
import jax
import jax.numpy as jnp

class Brain:
    


class SpikingNeuron:

    def fire(self, mem: jnp.ndarray) -> jnp.ndarray:
        """
        Generates a spike if mem > threshold.
        Returns a spike

        :param mem: membrane potential
        :return:
            spike
        """
        pass

    def fire_inhibition(self, batch_size, mem: jnp.ndarray) -> jnp.ndarray:
        """
        Generates a spike if mem > threshold but only for the largest membrane. All other neurons
            will be inhibited

        :param batch_size:
        :param mem:
        :return:
            spike
        """