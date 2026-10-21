import React, { Suspense, lazy } from "react";

export const load = <P extends object>(Component: React.ComponentType<P>) => {
  return (props: P) => (
    <Suspense fallback={<div>Loading...</div>}>
      <Component {...props} />
    </Suspense>
  );
};

export const loadLazy = <P extends object>(
  importFunc: () => Promise<{ default: React.ComponentType<P> }>,
) => {
  return load(lazy(importFunc));
};
