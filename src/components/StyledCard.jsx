import React from "react";
import styled from "styled-components";
// Icons
import { FaGithub } from "react-icons/fa";
// Media
import GH from "../images/GH.svg";
// Components
import { Card } from "react-bootstrap";

const StyledCardComponent = styled.div`
  .card-footer {
    border-top: var(--border);

    .card-link {
      text-decoration: none;
      font-size: 1.5rem;
      color: ${({ theme }) => theme.color};

      &:hover {
        color: var(--primary);
      }
    }
  }
`;

export default function StyledCard({ theme, image, name, description, url }) {
  return (
    <StyledCardComponent>
      <Card bg={theme === "light" ? "white" : "dark"}>
        <Card.Img
          variant="top"
          src={image ? image : GH}
          alt={name}
          className="mx-auto"
        />
        <Card.Body className="overflow-auto text-center">
          <Card.Title>{name}</Card.Title>
          <Card.Text>{description}</Card.Text>
        </Card.Body>
        <Card.Footer className="text-center">
          <Card.Link href={url}>
            {"View on GitHub "}
            <FaGithub />
          </Card.Link>
        </Card.Footer>
      </Card>
    </StyledCardComponent>
  );
}
