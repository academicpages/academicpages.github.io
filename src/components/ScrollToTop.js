import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useSelector } from "react-redux";
import { selectData } from "../pages/homeSlice";

export default function ScrollToTop() {
  const { pathname, hash, key } = useLocation();
  const { name } = useSelector(selectData);
  const navigate = useNavigate();

  React.useEffect(
    function () {
      // if not a hash link, scroll to top
      if (hash === "") {
        window.scrollTo(0, 0);
      }
      // else scroll to id
      else {
        const id = hash.replace("#", "");
        const element = document.getElementById(id);
        if (element) {
          element.scrollIntoView();
        } else {
          navigate("404", { replace: false });
        }
      }

      if (pathname === "/") {
        document.title = `${name} | Portfolio`;
      } else if (pathname === "/All-Projects") {
        document.title = `${name} | All Projects`;
      } else {
        document.title = `${name} | Portfolio`;
      }
    },
    [pathname, name, hash, key, navigate]
  );

  return null;
}
