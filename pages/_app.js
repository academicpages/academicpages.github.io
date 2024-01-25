import '../styles.css'

import { Provider as StyletronProvider } from "styletron-react";
import { Div, StyleReset, ThemeProvider } from "atomize";
import { styletron } from "../styletron";

const theme = {
  colors: {
    black900: "#1d1d1e",
    greyLight: "#f2f3f4",
    border: "#d1d1d1"
  },
};

export default function MyApp({ Component, pageProps }) {
  return (
    <StyletronProvider value={styletron}>
      <ThemeProvider theme={theme}>
        <StyleReset />
          <Div
            textColor="black900"
            rounded="br1"
            shadow="3"
            d="flex"
            textWeight="500"
            flexDir="column"
            p={{ x: "1rem", y: "1rem" }}
          >
        <Component {...pageProps} />
        </Div>
      </ThemeProvider>
    </StyletronProvider>
  );
}
