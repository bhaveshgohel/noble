{
  'targets': [
    {
      'target_name': 'hci-ble',
      'type': 'executable',
      'conditions': [
        ['OS=="linux"', {
          'sources': [
            'src/hci-ble.c'
          ],
          'link_settings': {
            'libraries': [
              '-lbluetooth'
            ]
          },
        }]
      ]
    }
  ]
}
