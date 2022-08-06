import styled from "styled-components";
// Components
import SocialLinks from "./SocialLinks";

const StyledFooter = styled.footer`
  min-height: var(--min-footer-height);
  background: var(--primary);

  a {
    color: #45413c;

    &:hover {
      color: #fbfdff;
    }
  }
`;

export default function Footer() {
  return (
    <StyledFooter className="d-flex align-items-center justify-content-center">
      <SocialLinks />
    </StyledFooter>
  );
}
