import { render, screen } from '@testing-library/react';
import App from './App';
import { shallow } from 'enzyme';

test('renders learn react link', () => {
  let wrapped = shallow(<App></App>);
  expect(wrapped).toMatchSnapshot();
});
