""" This file defines the sample list wrapper and sample writers. """
<<<<<<< HEAD
import _pickle as cPickle
=======
import pickle as cPickle
>>>>>>> ead669d6413f6a86abc0698b0f01603492fcdf30
import logging
import numpy as np

<<<<<<< HEAD
# from gps_pb2.gps_pb2 import NOISE
=======
# from gps.proto.gps_pb2 import NOISE
NOISE = 19
>>>>>>> ead669d6413f6a86abc0698b0f01603492fcdf30

LOGGER = logging.getLogger(__name__)


class SampleList(object):
    """ Class that handles writes and reads to sample data. """
    def __init__(self, samples):
        self._samples = samples

    def get_X(self, idx=None):
        """ Returns N x T x dX numpy array of states. """
        if idx is None:
            idx = range(len(self._samples))
        return np.asarray([self._samples[i].get_X() for i in idx])

    def get_U(self, idx=None):
        """ Returns N x T x dU numpy array of actions. """
        if idx is None:
            idx = range(len(self._samples))
        return np.asarray([self._samples[i].get_U() for i in idx])

    def get_noise(self, idx=None):
        """ Returns N x T x dU numpy array of noise generated during rollouts. """
        if idx is None:
            idx = range(len(self._samples))
        return np.asarray([self._samples[i].get(NOISE) for i in idx])

    def get_obs(self, idx=None):
        """ Returns N x T x dO numpy array of features. """
        if idx is None:
            idx = range(len(self._samples))
        return np.asarray([self._samples[i].get_obs() for i in idx])

    def get_samples(self, idx=None):
        """ Returns N sample objects. """
        if idx is None:
            idx = range(len(self._samples))
        return [self._samples[i] for i in idx]

    def num_samples(self):
        """ Returns number of samples. """
        return len(self._samples)

    # Convenience methods.
    def __len__(self):
        return self.num_samples()

    def __getitem__(self, idx):
        return self.get_samples([idx])[0]


class PickleSampleWriter(object):
    """ Pickles samples into data_file. """
    def __init__(self, data_file):
        self._data_file = data_file

    def write(self, samples):
        """ Write samples to data file. """
        with open(self._data_file, 'wb') as data_file:
            cPickle.dump(data_file, samples)


class SysOutWriter(object):
    """ Writes notifications to sysout on sample writes. """
    def __init__(self):
        pass

    def write(self, samples):
        """ Write number of samples to sysout. """
        LOGGER.debug('Collected %d samples', len(samples))