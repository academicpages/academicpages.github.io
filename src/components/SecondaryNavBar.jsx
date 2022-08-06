import { useState } from "react";
import { useAppContext } from "../appContext";
import { Link, useLocation } from "react-router-dom";
// Components
import { Container, Nav, Navbar } from "react-bootstrap";
import { ToggleSwitch, FixedNavSpacer } from "./globalStyledComponents";
// Images
import Logo from "../images/logo.svg";

export default function SecondaryNavBar() {
  const [isExpanded, setExpanded] = useState(false);
  const { pathname } = useLocation();
  const { theme } = useAppContext();

  return (
    <>
      <FixedNavSpacer />
      <Navbar
        id="nav"
        collapseOnSelect={true}
        expand="lg"
        expanded={isExpanded}
        bg={theme === "light" ? "white" : "dark"}
        variant={theme === "light" ? "light" : "dark"}
        fixed="top"
      >
        <Container>
          <Navbar.Brand>
            <img
              alt="React Logo"
              src={Logo}
              width="30"
              height="30"
              className="d-inline-block align-top bg-dark rounded-circle nav-logo"
            />
          </Navbar.Brand>
          <Navbar.Toggle
            aria-controls="responsive-navbar-nav"
            onClick={() => setExpanded(!isExpanded)}
          />
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav navbarScroll className="me-auto">
              <Nav.Item>
                <Link
                  to="/"
                  className={pathname === "/" ? "nav-link active" : "nav-link"}
                >
                  Home
                </Link>
              </Nav.Item>
              <Nav.Item>
                <Link
                  to="/All-Projects"
                  className={
                    pathname === "/All-Projects"
                      ? "nav-link active"
                      : "nav-link"
                  }
                >
                  All Projects
                </Link>
              </Nav.Item>
            </Nav>
            <Nav>
              <ToggleSwitch />
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </>
  );
}
