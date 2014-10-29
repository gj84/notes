Ubuntu Notes
============

Ubuntu 14.04 on Compaq
----------------------

Bug high temp:
  The gvfs-metadata is in a infinite loop for x reason. This kills and deletes metadata, and does the temp 20degrees less
  sudo killall gvfsd-metadata
  rm -rf ~/.local/share/gvfs-metadata
  
  .. _gvfs: http://manpages.ubuntu.com/manpages/saucy/man7/gvfs.7.html
  .. _forum: http://ubuntuforums.org/showthread.php?t=1421580
