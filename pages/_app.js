import { Provider as StyletronProvider } from "styletron-react";
import { styletron } from "../styletron";

import { ThemeProvider } from "atomize";

const theme = {
  colors: {
    black900: "#1d1d1e",
    greyLight: "#f2f3f4",
    border: "#d1d1d1"
  },
  rounded: {
    br1: "4px"
  }
};

export default function App({ Component, pageProps }) {
  return (
    <StyletronProvider value={styletron}>
      <ThemeProvider theme={theme}>
        <Component {...pageProps} />
      </ThemeProvider>
    </StyletronProvider>
  );
}
