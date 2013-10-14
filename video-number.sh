#! /bin/bash
sudo mount /dev/disk/by-id/usb-APPLE_SD_Card_Reader_000000009833-0:0-part1 /mnt/storage
echo last video filmed is $(ls /mnt/storage/PRIVATE/AVCHD/BDMV/STREAM | sort -n | tail -n 1)
sudo umount /mnt/storage
