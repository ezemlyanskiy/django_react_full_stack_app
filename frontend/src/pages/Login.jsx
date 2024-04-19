import Form from "../components/Form";

function Login() {
  return <Form route="api/v1/jwt/create/" method="login" />;
}

export default Login;
