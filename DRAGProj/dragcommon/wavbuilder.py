import os
from pydub import AudioSegment
from DRAGProj.dragcommon.audiothread import AudioThread
import DRAGProj.mappers.drummapper as dm

"""
A module that writes whole wav tracks from component wav instruments
and manages them.

    Author:
        James
    
    Version:
        3.1.0
        
    See:
        pydub.AudioSegment
"""


def open_wav(file_path):
    """
    A method that utilises the AudioSegment class to
    open a wav file.

    Args:
        file_path (:obj:`str`): A string representing the file to open.

    Returns:
        :obj:`AudioSegment`: An AudioSegment object containing the file.
    """
    return AudioSegment.from_wav(file_path)


def map_input(candidate, bpm, output_file, path):
    """
    Builds a wav track to write to the staticfiles dir.

    Args:
        candidate (:obj:`Track`): A Track object to use to write the file.
        bpm (int): A number representing the beats per minute or tempo of the track.
        output_file (:obj:`str`) : A string representing the file to write to.
        path (:obj:`str`): A string representing a combination of the website and staticfiles directories.

    See:
        DRAGProj.mappers.drummapper
    """
    output = AudioSegment.silent(duration=100)               # Initialise the track output
    gap = AudioSegment.silent(duration=beat_offset(bpm))     # Create a gap based on provided bpm.
    for instrument in candidate.content:
        file = dm.drum_mapper[instrument]                    # Get the correlating instrument to the int value.
        audio = open_wav(path + file)
        output = output.append(gap)                          # Start with a small gap to reduce edge fuzziness.
        output = output.append(audio)                        # Append the audio file to the track.
    begin_audio_thread(output, output_file, gap)


def begin_audio_thread(output, output_file, gap):
    """
    Begins an AudioThread and thus, the writing process of a wav file.

    Args:
        output (:obj:`AudioSegment`): The AudioSegment object representing the track to be written.
        output_file (:obj:`str`) : A string representing the file to write to.
        gap (:obj:`AudioSegment`): An AudioSegment object of a specified silence duration.

    See:
        DRAGProj.dragcommon.audiothread
    """
    output = output.append(gap)                              # append a gap to reduce fuzziness.
    thread = AudioThread(output, output_file)                # create an AudioThread to write the track.
    thread.start()


def beat_offset(bpm):
    """
    A function to return pauses between component wav files.
    Doing so allows adjustment of tempo to over 300 bpm.

    Args:
        bpm (int): A number representing the beats per minute or tempo of the track.

    Returns:
         number: A value indicating the space between notes in milliseconds, hence 60000.
    """
    minute_milliseconds = 60000
    return minute_milliseconds / bpm


def clear_wav_candidates(wav_directory, string):
    """
    A function to clear out old wav files from a previous generation.

    Args:
        wav_directory (:obj:`str`): A string representing the directory to clear of candidates.
        string (:obj:`str`): A string to match against files in the directory for deletion.

    See:
        os
    """
    for file in os.listdir(wav_directory):
        if string in file:
            os.remove(os.path.join(wav_directory, file))


