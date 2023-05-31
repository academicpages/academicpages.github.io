@function breakpoint-parse-default($feature) {
  $default: breakpoint-get('default feature');

  // Set Context
  $context-setter: private-breakpoint-set-context($default, $feature);

  @if (breakpoint-get('to ems') == true) and (type-of($feature) == 'number') {
    @return '#{$default}: #{breakpoint-to-base-em($feature)}';
  }
  @else {
    @return '#{$default}: #{$feature}';
  }
}
