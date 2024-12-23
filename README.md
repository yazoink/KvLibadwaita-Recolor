# KvLibadwaita Recolor
A small utility to quickly create KvLibadwaita themes.

## Usage
`git clone https://github.com/yazoink/KvLibadwaita-Recolor`     
`cd KvLibadwaita-Recolor`     
`./recolor.py path_to_new_palette.json new_theme_name`     

The new theme will appear in `./out`.

The palette JSON file should be structured like this:
```json
{
  "background00": "#1C1213",
  "background01": "#2A1C1B",
  "background02": "#30201F",
  "background03": "#462F2C",
  "background04": "#4D3431",
  "foreground00": "#A87569",
  "foreground01": "#C58D7B",
  "accent": "#893F45",
  "disabled_foreground": "#6D4745",
  "divider_color": "#4A2E2F"
}
```

There are some example schemes in `./colorschemes`

## Screenshots
![20241223_16:31:05_screenshot](https://github.com/user-attachments/assets/cb9593a7-9c3c-497b-b187-ad8f8aafb070)

