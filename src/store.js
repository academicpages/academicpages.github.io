// https://redux.js.org/tutorials/fundamentals/part-8-modern-redux#using-configurestore
import { configureStore } from "@reduxjs/toolkit";
//Reducers
import homeReducer from "./pages/homeSlice";
import allProjectsReducer from "./pages/allProjectsSlice";

export const store = configureStore({
  reducer: {
    home: homeReducer,
    allProjects: allProjectsReducer,
  },
});
