import React, { useState, useEffect } from "react";
import axiosInstance from "../axios";
import { useParams } from "react-router-dom";
// Material UI
import { CssBaseline, Container, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: "flex",
    flexdirection: "column",
    alignItems: "center",
  },
}));

const Post = () => {
  const { slug } = useParams();
  const classes = useStyles();
  const [data, setData] = useState({ posts: [] });

  useEffect(() => {
    axiosInstance.get(slug).then((res) => {
      setData({ posts: res.data });
      console.log(res.data);
    });
  }, [setData]);

  return (
    <Container component="main" maxWidth="md">
      <CssBaseline />
      <div classNamte={classes.paper}></div>
      <div className={classes.heroContent}>
        <Container maxWidth="sm">
          <Typography
            component="h1"
            variant="h2"
            align="center"
            color="textPrimary"
            gutterBottom
          >
            {data.posts.title}
          </Typography>
          <Typography
            variant="h5"
            align="center"
            color="textSecondary"
            paragraph
          >
            {data.posts.excerpt}
          </Typography>
        </Container>
      </div>
    </Container>
  );
};

export default Post;
