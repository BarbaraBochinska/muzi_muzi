import React, { Component } from "react";
import Adverts from "./Adverts";
import Users from "./Users";
import { Container } from "react-bootstrap";
import { Tabs } from "antd";

export default class News extends Component {
  render() {
    const { TabPane } = Tabs;

    function callback(key) {
      console.log(key);
    }
    return (
      <Container>
        <Tabs onChange={callback} type="card">
          <TabPane tab="Adverts" key="1">
            <Adverts />
          </TabPane>
          <TabPane tab="Users" key="2">
            <Users />
          </TabPane>
          <TabPane tab="Bands" key="3">
            Content of Tab Pane 3
          </TabPane>
        </Tabs>
      </Container>
    );
  }
}
