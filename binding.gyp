{
  "targets": [
    {
      "target_name": "node-rpio",
      "include_dirs": [ "<!(node -e \"require('nan')\")" ],
      "sources": [
        "src/bcm2835.c",
        "src/rpio.cc"
      ]
    }
  ]
}
