import { render, screen } from '@testing-library/react';
import App from './App';
import { shallow } from 'enzyme';

test('App renders properly without any error', () => {
  let wrapped = shallow(<App></App>);
  expect(wrapped).toMatchSnapshot();
});
