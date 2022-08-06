import React from "react";
import { useAppContext } from "../appContext";
import { useSelector } from "react-redux";
import { selectData, selectError, selectIsLoading } from "./allProjectsSlice";
import { Element } from "react-scroll";
import styled from "styled-components";
// Icons
import { FaGithub, FaSearch } from "react-icons/fa";
// Components
import { Col, Container, FormControl, InputGroup, Row } from "react-bootstrap";
import {
  BackToTop,
  Title,
  Loading,
} from "../components/globalStyledComponents";
import AllProjectsNavBar from "../components/SecondaryNavBar";
import StyledCard from "../components/StyledCard";
import Footer from "../components/Footer";

const StyledSection = styled.section`
  min-height: 90vh;
  padding-bottom: var(--nav-height);

  .input-group {
    max-width: 90vw;
  }

  .card-link {
    text-decoration: none;
    font-size: 1.5rem;
    color: ${({ theme }) => theme.color};

    &:hover {
      color: var(--primary);
    }
  }

  @media screen and (min-width: 800px) {
    .input-group {
      width: 75%;
    }
  }
`;

export default function AllProjects() {
  const [searchInput, setSearchInput] = React.useState("");
  const [filteredResults, setFilteredResults] = React.useState([]);
  const { theme } = useAppContext();
  const isLoading = useSelector(selectIsLoading);
  const error = useSelector(selectError);
  const data = useSelector(selectData);

  React.useEffect(
    function () {
      if (searchInput !== "") {
        const filteredData = data.filter((item) => {
          return item.name.toLowerCase().includes(searchInput.toLowerCase());
        });
        setFilteredResults(filteredData);
      } else {
        setFilteredResults(data);
      }
    },
    [searchInput, data]
  );

  if (isLoading) {
    return (
      <>
        <AllProjectsNavBar />
        <main>
          <StyledSection className="d-flex flex-column justify-content-center">
            <Container className="d-flex">
              <Title>
                <h2>
                  All <FaGithub /> Projects
                </h2>
                <div className="underline"></div>
              </Title>
            </Container>
            <Loading />
          </StyledSection>
        </main>
        <Footer />
      </>
    );
  } else if (error) {
    return (
      <>
        <AllProjectsNavBar />
        <main>
          <StyledSection className="d-flex flex-column justify-content-center">
            <Container className="d-flex">
              <Title>
                <h2>
                  All <FaGithub /> Projects
                </h2>
                <div className="underline"></div>
              </Title>
            </Container>
            <h2 className="my-5 text-center">{error}</h2>
          </StyledSection>
        </main>
        <Footer />
      </>
    );
  } else {
    return (
      <>
        <Element name={"AllProjects"}>
          <AllProjectsNavBar />
        </Element>
        <main>
          <StyledSection className="d-flex flex-column justify-content-center">
            <Container className="d-flex">
              <Title>
                <h2>
                  All <FaGithub /> Projects
                </h2>
                <div className="underline"></div>
              </Title>
            </Container>
            <Container>
              <InputGroup className="mx-auto mb-4">
                <InputGroup.Text id="search">
                  <FaSearch />
                </InputGroup.Text>
                <FormControl
                  placeholder="Project name"
                  aria-label="Search projects"
                  aria-describedby="search"
                  onChange={(e) => setSearchInput(e.currentTarget.value)}
                />
              </InputGroup>
              <Row xs={1} md={2} lg={3} className="g-4 justify-content-center">
                {searchInput.length > 0
                  ? filteredResults.map(function ({
                      id,
                      image,
                      name,
                      description,
                      html_url,
                    }) {
                      return (
                        <Col key={id}>
                          <StyledCard
                            theme={theme}
                            image={image}
                            name={name}
                            description={description}
                            url={html_url}
                          />
                        </Col>
                      );
                    })
                  : data.map(function ({
                      id,
                      image,
                      name,
                      description,
                      html_url,
                    }) {
                      return (
                        <Col key={id}>
                          <StyledCard
                            theme={theme}
                            image={image}
                            name={name}
                            description={description}
                            url={html_url}
                          />
                        </Col>
                      );
                    })}
              </Row>
            </Container>
          </StyledSection>
        </main>
        <BackToTop home={"AllProjects"} />
        <Footer />
      </>
    );
  }
}
